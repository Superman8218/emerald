from django.shortcuts import render_to_response
from django.template import RequestContext

from models import FboMaster

# Create your views here.

def detail(request):
    return render_to_response(
            'data/detail.html',
            {
                'data': FboMaster.objects.all()[:10],
                'count':FboMaster.objects.count()
            },
            context_instance=RequestContext(request)
    )
