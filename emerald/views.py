from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from data.models import FboMaster
import data.FboImport as imp

def index(request):
    return render_to_response('emerald/index.html')

def test(request):
    imp.main()
    return HttpResponse("Test successful")

def landing(request):
    return render_to_response('emerald/landing-page-email-list.html')

def displayFbo(request):
    return render_to_response('emerald/display-Fbo.html', { 'data':FboMaster.objects.all()[:10], 'count':FboMaster.objects.count() }, RequestContext(request))
