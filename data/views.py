from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import DetailView, ListView

from models import FboMaster

import FboImport

# Create your views here.

def FboImportView(request):
    FboImport.main()
    return HttpResponse("Import was successful")

class FboDetailView(DetailView):

    model = FboMaster
    template_name = 'data/fbo-detail.html'

    # def get(self, request, fbo_master_id):
        # fbo_master = FboMaster.objects.get(pk=fbo_master_id)
        # return render(request, 'data/fbo-detail.html',
                # {
                    # 'fbo_master': fbo_master
                # }
            # )

class FboListView(ListView):

    model = FboMaster
    template_name = 'data/fbo-list.html'
