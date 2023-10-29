from datetime import timezone
import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.


class User(AbstractUser):

    gender = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'All'),
    ]

    username = None
    uid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    email_is_verified = models.BooleanField(default=False)
    clg_email = models.EmailField(blank=True)
    # clgEmail_is_verified = models.BooleanField(default=False)
    mobile = models.CharField(max_length=14)
    # clgEmail_token = models.CharField(max_length=100, null=True, blank=True)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_logout_time = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(choices=gender, null=True, max_length=1)
    user_image = models.ImageField(null=True, blank=True, upload_to="profilePicture/")  # , default="")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    # return self.first_name + self.last_name
