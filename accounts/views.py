from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from django.contrib import messages

from accounts.forms import *
from accounts.models import *


# Create your views here.


# REGISTRATION VIEW - FORM VIEW#

class UserRegistration(CreateView):
    model = UserRegistrationInfo
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            customer_email=form.cleaned_data["customer_email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


# REGISTRATION REDIRECT VIEW - PROFILE REDIRECT #

@method_decorator(login_required, name='dispatch')
class UserProfile(TemplateView):
    template_name = 'accounts/user_profile.html'


# LOGIN VIEW #

class UserLogin(LoginView):
    authentication_form = UserLogin
    template_name = 'accounts/user_login.html'
    success_url = '/accounts/profile/'

# LOGOUT VIEW #


class UserLogout(LogoutView):
    template_name = 'accounts/user_logout.html'


# PASSWORD OPERATIONS#
# USER PASSWORD CHANGE - CHANGE #

@method_decorator(login_required, name='dispatch')
class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'accounts/user_password_change.html'
    success_url = '/accounts/passwordchanged/'


# USER PASSWORD CHANGE - CHANGED SUCCESSFULLY #
@method_decorator(login_required, name='dispatch')
class UserPasswordChangedView(PasswordChangeDoneView):
    template_name = 'accounts/user_password_change_done.html'


# USER PASSWORD RESET - RESET FORM VIEW#

class UserRestPassword(PasswordResetForm):
    pass


# USER PASSWORD RESET - REST DONE VIEW #

class UserSetPassword(SetPasswordForm):
    pass
