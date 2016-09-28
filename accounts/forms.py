from django import forms
from django.contrib.auth.forms import UserCreationForm

class EmeraldGovRegistrationForm(UserCreationForm):
    username = forms.CharField(
            label='Username',
            widget=forms.TextInput(attrs=
                {
                    'class':'form-control',
                    'name':'username',
                    'placeholder':'Username',
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
