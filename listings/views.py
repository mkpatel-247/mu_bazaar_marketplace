from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import *
from .models import *
from accounts.models import User
from django.db.models import Count, Q

# addProduct
# updateProduct
# disableProduct


@login_required(login_url='/sign_in/')
def new_ad_listing(request, uid):

    userDetails = User.objects.get(uid=uid)
    if request.method == 'GET':
        # cat_models_details = Category()
        details = Category.objects.all()
        city_details = ads.city
        # User.get_session_auth_hash
        return render(request, 'ad-listing.html', {'cat': details, 'userData': userDetails, 'city': city_details})

    if request.method == 'POST':
        title = request.POST.get('ads_title')
        gender = request.POST.get('gender')  # currently not in use
        cat_id = request.POST.get('adscategory')
        item_price = request.POST.get('price')
        description = request.POST.get('ads-description')
        nego = request.POST.get('is_negotiable')
        mainImage = request.FILES.get('mainImagesFile')
        print(nego)
        address = request.POST.get('ads_location')
        if nego == None:
            nego = False

        cat_id = Category.objects.get(cat_uid=cat_id)
        # for image in images:
        try:
            listing = ads.objects.create(
                ads_title=title,
                ads_description=description,
                price=item_price,
                category_id=cat_id,
                negotiable=nego,
                owner=userDetails,
                first_ads_images=mainImage,
                location=address,
                adsForWhichGender=gender
            )
            # if listing is not None:
            images = request.FILES.getlist('imagesFile')
            print(images)
            for imgs in images:
                product_image = Ads_Images.objects.create(
                    ads_id=listing,
                    ads_photos=imgs
                )
                print(product_image, " ", imgs)
                # if product_image is not None:
                # product_image.save()
        except Exception as e:
            print('Error : ', e)
        return redirect(f'/dashboard/{uid}/')


@login_required(login_url='/sign_in/')
def single_page_ads(request, id):
    if request.method == 'GET':
        # userDetails = ads.objects.get(owner=uid)
        adsDetails = ads.objects.get(ads_id=id)
        userImage = User.objects.get(email=adsDetails.owner)
        wishlistobj = Wishlist.objects.all().filter(user_id=request.user, ads_id=id)
        print(adsDetails.listed_date)
        adsImages = Ads_Images.objects.all().filter(ads_id=adsDetails)
        OnlyOneImage = False
        if len(adsImages) <= 1:
            OnlyOneImage = True
        print(len(adsImages))
        obj = Wishlist.objects.all()
        print(adsDetails.location)
    return render(request, 'single-page-ads.html', {'details': adsDetails, 'image': adsImages, 'userImage': userImage, 'isWishlist_exist' : wishlistobj, 'oneImage' : OnlyOneImage})

@login_required(login_url='/sign_in/')
def update_listing(request, uid, aid):
    # pass
    updateAds = get_object_or_404(ads, ads_id=aid)
    if request.method == "POST":

        self = updateAds
        chk = uid
        title = request.POST.get('ads_title')
        gender = request.POST.get('gender')
        description = request.POST.get('ads-description')
        ads_publish = request.POST.get('published')
        cat_id = request.POST.get('adscategory')
        item_price = request.POST.get('price')
        nego = request.POST.get('is_negotiable')
        address = request.POST.get('ads_location')

        print(str(cat_id) + " " + str(updateAds.category_id))
        print(nego)
        if updateAds.ads_title != title:
            updateAds.ads_title = title
            chk = ads.save(self, update_fields=['ads_title'])
        
        if updateAds.adsForWhichGender != gender:
            updateAds.adsForWhichGender = gender
            chk = ads.save(self, update_fields=['adsForWhichGender'])
        
        if updateAds.ads_description != description:
            updateAds.ads_description = description
            chk = ads.save(self, update_fields=['ads_description'])
            
        if ads_publish == "Yes":
            updateAds.is_published = True
            chk = ads.save(self, update_fields=['is_published'])
        elif ads_publish == "No":
            updateAds.is_published = False
            print("Coming.....")
            chk = ads.save(self, update_fields=['is_published'])

        if updateAds.category_id.cat_uid != cat_id:
            category = Category.objects.get(cat_uid=cat_id)
            updateAds.category_id = category
            chk = ads.save(self, update_fields=['category_id'])
        
        if updateAds.price != item_price:
            updateAds.price = item_price
            chk = ads.save(self, update_fields=['price'])
        
        if nego == None:
            updateAds.negotiable = False
            chk = ads.save(self, update_fields=['negotiable'])
        elif nego == "on":
            updateAds.negotiable = True
            chk = ads.save(self, update_fields=['negotiable'])

        if updateAds.location != address:
            updateAds.location = address
            chk = ads.save(self, update_fields=['location'])

        print(updateAds.last_modified)
        if chk == None:
            messages.success(request, "Record Updated")
        else:
            messages.error(request, "Record Not Updated")

        # try:
        #     mainImage = request.FILES.get('mainImage')
        #     images = request.FILES.getlist('images')
        # except Exception as e:

    return redirect(f'/dashboard/{uid}/')


@login_required(login_url='/sign_in/')
def delete_listing(request, uid, aid):
    # if request.method == 'POST':
    listing = ads.objects.get(owner=uid, ads_id=aid)
    print(f'{listing} {listing.ads_id}')

    temp = listing.delete()
    print(temp)
    # return HttpResponse(f'{temp} {listing} {aid}')
    return redirect(f'/dashboard/{uid}/')


def all_listing(request):
    if request.method == "GET":
        listing = ads.objects.all().filter(Q(is_published=True) & Q(adsForWhichGender=request.user.gender) | Q(adsForWhichGender="A") | Q(owner = request.user))
        categories = Category.objects.all()
        
        cat_count = ads.objects.values('category_id').annotate(num_Category=Count('category_id'))
        items = Category.objects.annotate(quantity=Count('cat_uid'))
        print(cat_count)
        cnt_cat = list()
        # print(cat_count)
        # k = 0
        for i in cat_count:
            cnt_cat.append(i.get('num_Category'))
        
        print(cnt_cat)
        # listing_Image = Ads_Images.objects.all()
        print(categories)
        return render(request, 'listing.html', {"ads": listing, "cat":categories, 'cat_count':cnt_cat})
    # if request.method == "POST":

@login_required(login_url='/sign_in/')
def search_listing(request):
    categories = Category.objects.all()
    logic = (Q(is_published=True) & Q(adsForWhichGender=request.user.gender) | Q(adsForWhichGender="A") | Q(owner = request.user))
    if request.method == 'GET':
        query = request.GET.get('queryName')
        print(query)
        if query == '' or len(query) < 2:
            referring_page = request.META.get('HTTP_REFERER')
            messages.warning(request, "Search is empty write atleast 3 letters to get appropriate result")
            return redirect(referring_page)
        else:
            # print(query)
            # categoryQuery = Category.objects.get(category_name=query)
            # print(categoryQuery)
            # logic = (Q(is_published=True) & Q(adsForWhichGender=request.user.gender) | Q(adsForWhichGender="A") | Q(owner = request.user))
            # if categoryQuery != None:
            #     listings = ads.objects.filter(logic).filter(category_id=categoryQuery)
            #     # record_Count = len(listings)
            #     print(listings)
            #     record_Count = 0
            # else:    
            print("Inside Else =", query)
            
            listings = ads.objects.filter(logic).filter(Q(ads_title__icontains = query) | Q(ads_description__icontains=query) | Q(location__icontains=query))
            
            record_Count = len(listings)
            return render(request, 'search-page.html', {'result' : listings, 'query' : query, 'noOfRecords': record_Count, 'cat':categories})
    if request.method == "POST":
        query = request.POST.get('queryName')
        print(query)
        categoryQuery = Category.objects.get(category_name=query)
        print(categoryQuery)
        
        if categoryQuery != None:
            listings = ads.objects.filter(logic).filter(category_id=categoryQuery)                
            record_Count = len(listings)
            print(listings)
            # record_Count = 0
        return render(request, 'search-page.html', {'result' : listings, 'query' : query, 'noOfRecords': record_Count, 'cat':categories})
    
@login_required(login_url='/sign_in/')
def wishlist_view(request, ads_id):
    listing_exist = ads.objects.get(ads_id=ads_id)
    print(listing_exist)
    if request.method == 'POST':
        getSymbol = request.POST.get('symbol')
        print("Error :" + ads_id)
        if listing_exist and getSymbol == "ADDED":
            Wishlist.objects.create(user_id=request.user, ads_id=listing_exist)
            print(listing_exist)
            messages.success(request, 'Added to Wishlist')
        
        elif listing_exist and getSymbol == "REMOVED":
            delete_wishlist_entry = Wishlist.objects.get(user_id=request.user, ads_id=listing_exist)
            delete_wishlist_entry.delete()
            messages.error(request, 'Removed from Wishlist')
        
        else:
            messages.error(request, 'Something went wrong')
    return redirect(f'/ads/{ads_id}')
