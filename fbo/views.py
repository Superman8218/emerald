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
from forms import FboMasterFilterFormHelper
from filters import FboMasterFilter

import pdb

# Create your views here.

class FboDetailView(LoginRequiredMixin, DetailView):

    model = FboMaster
    template_name = 'fbo/fbo-detail.html'

# Generic filtered table view

class FilteredSingleTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        self.filter = self.filter_class(self.request.GET, queryset=super(FilteredSingleTableView, self).get_table_data())
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)

        self.filter.form.helper = self.helper_class()
        context['filter'] = self.filter
        return context

class FboListView(FilteredSingleTableView, LoginRequiredMixin, ListView):

    model = FboMaster
    template_name = 'fbo/fbo-list.html'
    # template_name = 'fbo/fbo-list-old.html'
    table_class = FboMasterTable
    filter_class = FboMasterFilter
    helper_class = FboMasterFilterFormHelper

# Implements the magic view

class FboMagicView(FboListView):
    def get_context_data(self, **kwargs):
        context = super(FboMagicView, self).get_context_data(**kwargs)
        return context

    def get_table_data(self):
        qs = super(FboMagicView, self).get_table_data()
        return qs.filter(solicitation_type='presol')

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
    template_name = 'fbo/opportunity-detail.html'

class OpportunityListView(LoginRequiredMixin, SingleTableView, ListView):

    model = Opportunity
    template_name = 'fbo/opportunity-list.html'
    table_class = OpportunityTable

    # Only list the opportunites that belong to the logged in user's account

    def get_queryset(self):
        return Opportunity.objects.filter(account=self.request.user.userprofile.account)
