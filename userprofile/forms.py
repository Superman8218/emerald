from django import forms
from django.forms import ModelForm

from models import UserProfile

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['sam']
