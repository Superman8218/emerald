from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import DetailView, ListView

from models import FboMaster, Opportunity

import FboImport

# Create your views here.

def FboImportView(request):
    FboImport.main()
    return HttpResponse("Import was successful")

class FboDetailView(DetailView):

    model = FboMaster
    template_name = 'data/fbo-detail.html'

class FboListView(ListView):

    model = FboMaster
    template_name = 'data/fbo-list.html'

class OpportunityDetailView(DetailView):

    model = Opportunity
    template_name = 'data/opportunity-detail.html'

class OpportunityListView(ListView):

    model = Opportunity
    template_name = 'data/opportunity-list.html'

    # Only list the opportunites that belong to the logged in user's account

    def get_queryset(self):
        return Opportunity.objects.filter(account=self.request.user.userprofile.account)
