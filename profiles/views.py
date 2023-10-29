from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import *
from accounts.models import User
from listings.models import ads, Category, Wishlist
from django.contrib import messages


# Create your views here.


@login_required(login_url='/sign_in/')
def profile(request, uid):
    # ent = User.email.get()
    chk=uid
    if request.method == "GET":
        # row = request.objects.get('username': email)
        userDetails = User.objects.get(uid=chk)
        print(userDetails.user_image)
        return render(request, 'userProfile.html', {"data": userDetails})
    
    if request.method == "POST":
        updateUser = get_object_or_404(User, uid=chk)
        self = updateUser
        print(updateUser)
        print("Image here: "+str(updateUser.user_image))
        
        try:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            profileImage = request.FILES.get('profilePicture')
        
        except Exception as e:
            print("Exception Image : " + str(updateUser.user_image))
            profileImage = updateUser.user_image

        print("Updated Image here: " + str(profileImage))

        #Condition for First Name
        if updateUser.first_name == firstName:
            print("No updation in first Name bcoz it's find similar names")
        else:
            print("Updating first Name")
            updateUser.first_name = firstName
            chk = User.save(self, update_fields=['first_name'])

        
        #Condition for Last Name
        if updateUser.last_name == lastName:
            print("No updation in last Name bcoz it's find similar name")
        else:
            print("Updating Last Name")
            updateUser.last_name = lastName
            chk = User.save(self, update_fields=['last_name'])

        # print(str(profile))
        # print(len(str(profileImage)))

        if updateUser.user_image == profileImage or profileImage == None:
            print("No change in Image")
        else:
            updateUser.user_image.delete()
            updateUser.user_image = profileImage
            print("Updated Image here: " + str(updateUser.user_image))
            # chk = profileImage
            chk = User.save(self, update_fields=['user_image'])
                   
        if chk == None:
            messages.success(request, "Record Updated")
        else:
            messages.error(request, "Record Not Updated")

        return redirect(f'/profile/{uid}')


@login_required(login_url='/sign_in/')
def dashboard(request, uid):
    if request.method == "GET":
        userDetails = User.objects.get(uid=uid)
        category = Category.objects.all()
        listingDetails = ads.objects.all().filter(owner=uid).order_by('-listed_date')
        locations = ads.city

    return render(request, 'dashboard.html', {"data": userDetails, "listing": listingDetails, "cat" : category, "city" : locations})


@login_required(login_url='/sign_in/')
def wishlist(request):
    userDetails = User.objects.get(email=request.user)
    all_wishlist_ads = Wishlist.objects.filter(user_id=request.user)
    
    return render(request, 'user-wishlist.html', {"data": userDetails, 'wishlist_items':all_wishlist_ads})

'''
@login_required(login_url='/sign_in/')
def profilePersonalUpdate(request, uid):
    chk = uid
    if request.method == "POST":
        updateUser = User.objects.get(uid=chk)
        print(updateUser)
        print("Image here: "+str(updateUser.user_image))
        
        try:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            profileImage = request.FILES.getlist('profilePicture')
        
        except Exception as e:
            print("Exception Image : " + str(updateUser.user_image))
            profileImage = updateUser.user_image

        print("Updated Image here: " + str(profileImage))

        #Condition for First Name
        if updateUser.first_name == firstName:
            print("No updation in first Name bcoz it's find similar names")
        else:
            print("Updating first Name")
            updateUser.first_name = firstName
        
        #Condition for Last Name
        if updateUser.last_name == lastName:
            print("No updation in last Name bcoz it's find similar name")
        else:
            print("Updating Last Name")
            updateUser.last_name = lastName

        # print(str(setUser.user_image))
        # print(len(profileImage))
        if updateUser.user_image == profileImage or len(profileImage) == 0:
            print("No change in Image")
        else:
            updateUser.user_image.delete()
            updateUser.user_image = profileImage
            print("Image got updated...")
                   
        chk = updateUser.save()
        if chk != None:
            messages.success(request, "Record Updated")
        else:
            messages.error(request, "Record Not Updated")

    return redirect(f'/profile/{uid}')
'''

@login_required(login_url='/sign_in/')
def inbox(request):
    userDetails = User.objects.get(email=request.user)

    return render(request, 'queries-page.html', {'data' : userDetails})