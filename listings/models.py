from datetime import datetime
import uuid
from django.db import models
from accounts.models import User
# from .manager import ListingManager
# Create your models here.


class Category(models.Model):
    cat_uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=30, blank=False)
    category_desc = models.TextField(max_length=150, blank=True)
    category_slug = models.SlugField(max_length=30)
    created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.category_name

class ads(models.Model):

    Category.objects.all()
    User.objects.all()

    city = [
        ('Rajkot','Raj'),
        ('Morbi', 'Mor'),
        ('Jamnagar', 'Jam'),
        ('Junagadh','Jun'),
        ('Gandhinagar', 'GNR'),
        ('Gandhidham', 'Gandhidham, Kutch'),
        ('Bedi','Bedi, Rajkot'),
        ('Chotila','Chotila, Rajkot'),
        ('Gondal', 'gondal'),
    ]

    gender = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'All'),
    ]
    ads_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    ads_title = models.CharField(max_length=30, null=False, blank=False)
    ads_description = models.TextField(max_length=450, blank=True, null=False)
    price = models.IntegerField(null=False, blank=False, default=1)
    category_id = models.ForeignKey(Category, null=True, blank=True, db_column='cat_uid', on_delete=models.CASCADE)
    negotiable = models.BooleanField(null=True, blank=True, default=False)
    # address = models.TextChoices()
    owner = models.ForeignKey(
        User, null=True, blank=False, db_column='uid', on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    listed_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    # time = models.TimeField(default=datetime.now, null=True, blank=True)
    # no_of_likes = models.IntegerField(blank=True, null=True, default=0)
    location = models.CharField(choices=city, null=True, max_length=20)
    adsForWhichGender = models.CharField(choices=gender, null=True, max_length=1)
    first_ads_images = models.ImageField(upload_to="ads_list/", default="")
    # tags = models.ManyToManyField(tags)

    ordering = ['listed_date']
    def __str__(self):
        return self.ads_title


class Wishlist(models.Model):

    ads.objects.all()
    # User.objects.all()

    ads_id = models.ForeignKey(
        ads, db_column='ads_id', null=True, blank=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User, null=True, blank=True, db_column='uid', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ads_id} {self.user_id.first_name}'
    


class Ads_Images(models.Model):
    # User.objects.all()
    # ads.objects.all()
    ads_id = models.ForeignKey(
        ads, db_column='ads_id', on_delete=models.CASCADE, null=True)
    ads_photos = models.ImageField(upload_to="ads_list")

    def __str__(self):
        return str((f'{self.ads_id} {self.id}'))
# class Listings(models.Model):

    #     @classmethod
    #     def add_product():
    #         p_id = models.models.UUIDField(_("uuid4"))
    #         product_name = models.CharField(max_length=100)
