from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from fbo.models import FboMaster

import pdb

def index(request):
    return render(request, 'emerald/index.html')

def test(request):
    imp.main();
    return HttpResponse("Test successful")

def landing(request):
    return render(request, 'emerald/landing-page-email-list.html')
