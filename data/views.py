from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View, DetailView, ListView

from django_tables2 import SingleTableView

from models import FboMaster, Opportunity
from tables import FboMasterTable, OpportunityTable
import FboImport

import pdb

# Create your views here.

def FboImportView(request):
    FboImport.main()
    return HttpResponse("Import was successful")

class FboDetailView(LoginRequiredMixin, DetailView):

    model = FboMaster
    template_name = 'data/fbo-detail.html'

class FboListView(LoginRequiredMixin, SingleTableView, ListView):

    model = FboMaster
    template_name = 'data/fbo-list.html'
    table_class = FboMasterTable

def FboAddView(request, pk):

    # Get the information necessary to create a new opportunity

    opportunityFboMaster = FboMaster.objects.get(pk=pk)
    opportunityAccount = request.user.userprofile.account 

    # Create the new opportunity

    newOpportunity = Opportunity.objects.create(fbomaster=opportunityFboMaster, account=opportunityAccount)

    # Go to the new opportunity record

    return HttpResponseRedirect(reverse('opportunity-detail', kwargs={'pk':newOpportunity.id}))

class OpportunityDetailView(LoginRequiredMixin, DetailView):

    model = Opportunity
    template_name = 'data/opportunity-detail.html'

class OpportunityListView(LoginRequiredMixin, SingleTableView, ListView):

    model = Opportunity
    template_name = 'data/opportunity-list.html'
    table_class = OpportunityTable

    # Only list the opportunites that belong to the logged in user's account

    def get_queryset(self):
        return Opportunity.objects.filter(account=self.request.user.userprofile.account)
