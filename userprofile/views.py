from django.shortcuts import render

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import UpdateView

from forms import UserProfileUpdateForm
from accounts.models import EmeraldUser
from accounts.forms import UserUpdateForm
from models import UserProfile

import pdb

# Create your views here.

# class UserProfileUpdateView(View):

    # model = UserProfile
    # template_name = 'userprofile/update.html'
    # form_class = UserProfileUpdateForm

    # def get_success_url(self):
        # return reverse('home')

    # def get(self, request, pk):
        # userprofile = UserProfile.objects.get(pk=pk)
        # user = userprofile.user
        # user_form = UserUpdateForm(instance=user)
        # user_profile_form = UserProfileUpdateForm(instance = userprofile)

def UserProfileUpdateView(request, pk):

    userprofile = UserProfile.objects.get(pk=pk)
    user = userprofile.user
    user_form = UserUpdateForm()
    user_profile_form = UserProfileUpdateForm()

    if request.POST:

        user_form = UserUpdateForm(request.POST, instance=user)
        user_profile_form = UserProfileUpdateForm(request.POST, instance=userprofile)

        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()

        return HttpResponseRedirect(reverse('home'))

    user_form = UserUpdateForm(instance=user)
    user_profile_form = UserProfileUpdateForm(instance = userprofile)


    return render(request, 'userprofile/update.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
    })
