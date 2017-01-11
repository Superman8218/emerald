from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import EmeraldUser

import pdb

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

class EmeraldGovRegistrationForm(EmeraldUserCreationForm):
    email = forms.CharField(
            label='Email',
            widget=forms.TextInput(attrs=
                {
                    'class':'form-control',
                    'name':'email',
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

    def __init__(self, *args, **kwargs):
        super(EmeraldGovRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'email',
            'password1',
            'password2'
        ]

    class Meta:
        model = EmeraldUser
        fields = ()
