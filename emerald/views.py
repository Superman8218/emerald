from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from fbo.models import FboMaster

import pdb

def index(request):
    account_id = 0
    if request.user.is_authenticated():
        account_id = request.user.userprofile.account.id
    return render(request, 'emerald/index.html', {
        'account_id': account_id, 
    })

def test(request):
    imp.main();
    return HttpResponse("Test successful")

def landing(request):
    return render(request, 'emerald/landing-page-email-list.html')
