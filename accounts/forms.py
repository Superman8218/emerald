from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from accounts.models import EmeraldUser

import pdb

class UserFormMixin(forms.Form):

    email = forms.EmailField(
            label='Email',
            widget=forms.EmailInput(attrs=
                {
                    'class':'form-control',
                    'name':'username',
                    'placeholder':'Email Address',
                    'size':'50'
                })
            )

    password1 = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(attrs=
                {
                    'class':'form-control',
                    'name':'password1',
                    'placeholder':'Password',
                    'size':'50'
                })
            )

    password2 = forms.CharField(
            label='Password (again)',
            widget=forms.PasswordInput(attrs=
                {
                    'class':'form-control',
                    'name':'password2',
                    'placeholder':'Password',
                    'size':'50'
                })
            )

class EmeraldGovRegistrationForm(UserFormMixin, UserCreationForm):

    def __init__(self, *args, **kwargs):
        # pdb.set_trace()
        super(EmeraldGovRegistrationForm, self).__init__(*args, **kwargs)
        self.order_fields(['email', 'password1', 'password2'])


    class Meta:
        model = EmeraldUser
        fields = ['email', 'password1', 'password2']

class EmeraldUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(EmeraldUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = EmeraldUser
        fields = ("email",)

class EmeraldUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(EmeraldUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = EmeraldUser
        fields = ("email",)

class UserUpdateForm(ModelForm):

    first_name = forms.CharField(
            label='First Name',
            widget=forms.TextInput(attrs=
                {
                    'class':'form-control',
                    'name':'first_name',
                    'placeholder':'First Name',
                    'size':'50'
                })
            )

    last_name = forms.CharField(
            label='Last Name',
            widget=forms.TextInput(attrs=
                {
                    'class':'form-control',
                    'name':'last_name',
                    'placeholder':'Last Name',
                    'size':'50'
                })
            )

    email = forms.EmailField(
            label='Email',
            widget=forms.EmailInput(attrs=
                {
                    'class':'form-control',
                    'name':'email',
                    'placeholder':'Email Address',
                    'size':'50'
                })
            )

    class Meta:
        model = EmeraldUser
        fields = ['first_name', 'last_name', 'email']
