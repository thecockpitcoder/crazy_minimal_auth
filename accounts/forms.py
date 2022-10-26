from django import forms
from accounts.models import UserRegistrationInfo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, \
    PasswordResetForm, UserChangeForm, SetPasswordForm


class UserRegistrationForm(UserCreationForm):
    customer_email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control bg-secondary text-light'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-light'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-secondary text-light'}))

    class Meta:
        model = UserRegistrationInfo
        fields = ['first_name', 'middle_name', 'last_name', 'customer_email', 'customer_phone', 'password1',
                  'password2']
        labels = {'first_name': 'First Name', 'middle_name': 'Middle Name', 'last_name': 'Last Name',
                  'customer_email': 'Email',
                  'customer_phone': 'Phone Number', 'password1': 'Password', 'password2': 'Confirm Password'}
        widgets = {
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control bg-secondary text-light', 'placeholder': '********'}),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control bg-secondary text-light', 'placeholder': '********'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control bg-secondary text-light', 'placeholder': 'John'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg-secondary text-light', 'placeholder': 'Doe'}),
            'customer_phone': forms.TextInput(
                attrs={'class': 'form-control bg-secondary text-light', 'placeholder': '10-Digits Only'}),
        }


class UserLogin(AuthenticationForm):
    username = UsernameField(label='Email', widget=forms.TextInput(
        attrs={"autofocus": True, 'class': 'form-control bg-secondary text-light', 'placeholder': 'brezyy@mail.com'}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': 'form-control bg-secondary text-light',
                   'placeholder': '********'})
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '********', 'autofocus': True}))

    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Min 8 Characters'}))
    new_password2 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Min 8 Characters'}))


class UserPaswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Verification Email')


# User SET Password - Reset Password #

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Min. 8 Characters', 'autofocus': True}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control    ', 'placeholder': 'Min. 8 Characters', 'autofocus': True}))
