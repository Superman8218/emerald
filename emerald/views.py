from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('emerald/index.html')

def landing(request):
    return render_to_response('emerald/landing-page-email-list.html')
