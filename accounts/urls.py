from django.urls import path
from accounts.views import *

urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('changepassword/', UserPasswordChangeView.as_view(), name='changepassword'),
    path('passwordchanged/', UserPasswordChangedView.as_view(), name='passwordchanged'),
    path('resetpassword/', UserPasswordChangedView.as_view(), name='resetpassword'),
    path('resetpassworddone/', UserPasswordChangedView.as_view(), name='resetpassworddone'),
]