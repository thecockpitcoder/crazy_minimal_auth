from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from accounts.managers import UserRegistrationInfoMangers

# Create your models here.


class UserRegistrationInfo(AbstractBaseUser, PermissionsMixin):
    unique_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    customer_email = models.EmailField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    customer_phone = models.CharField(max_length=15, unique=True, null=False, blank=False)
    user_profile_photo = models.ImageField(upload_to='profile_photo', null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    email_verified = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    phone_verified = models.BooleanField(default=False)
    hide_phone_num = models.BooleanField(default=True)
    profile_verified = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    is_premium_plus = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'customer_email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'customer_phone']

    objects = UserRegistrationInfoMangers()

    def __str__(self):
        return self.customer_email
