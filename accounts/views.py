from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import UpdateView

from models import Account
from forms import EmeraldGovRegistrationForm

import pdb

def register(request):
    form = EmeraldGovRegistrationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()
        new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                               )
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/register.html', {
        'form': form
    })

class LoginView(View):
    def get(self, request):
        args = {}
        if 'next' in request.GET:
            args['next'] = request.GET['next']
        return render(request, 'accounts/login.html', args)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    redirectUrl = request.POST['next']
                else:
                    redirectUrl = reverse('home')
                return HttpResponseRedirect(redirectUrl)
            else:
                return HttpResponse("Your EmeraldGov account is disabled")
        else:
            print 'Invalid login details: {0}, {1}'.format(username, password)
            return HttpResponse("Invalid login details supplied.")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

class AccountUpdate(UpdateView):

    model = Account
    template_name = 'accounts/update.html'
    fields = ['name', 'sam']
