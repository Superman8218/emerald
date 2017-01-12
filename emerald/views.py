from django.shortcuts import render

import pdb

def index(request):
    return render(request, 'emerald/index.html')

def landing(request):
    return render(request, 'emerald/landing-page-email-list.html')
