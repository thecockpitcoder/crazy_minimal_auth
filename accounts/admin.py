from django.contrib import admin
from accounts.models import UserRegistrationInfo

# Register your models here.


@admin.register(UserRegistrationInfo)
class UserRegistrationInfoAdmin(admin.ModelAdmin):
    list_display = ['unique_id', 'customer_email', 'password', 'first_name', 'middle_name', 'last_name',
                    'customer_phone', 'user_profile_photo', 'email_verified', 'phone_verified', 'profile_verified',
                    'is_premium', 'is_premium_plus', 'hide_email', 'hide_phone_num', 'registration_date', 'last_login',
                    'is_active', 'is_staff', 'is_superuser']