from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View, DetailView, ListView

from emerald.views import FilteredSingleTableView
from models import FboMaster
from tables import FboMasterTable
from forms import FboMasterFilterFormHelper
from filters import FboMasterFilter

import pdb


class FboDetailView(LoginRequiredMixin, DetailView):

    model = FboMaster
    template_name = 'fbo/fbo-detail.html'

class FboListView(FilteredSingleTableView, LoginRequiredMixin, ListView):

    model = FboMaster
    template_name = 'fbo/fbo-list.html'
    table_class = FboMasterTable
    filter_class = FboMasterFilter
    helper_class = FboMasterFilterFormHelper

# Implements the magic view

class FboMagicView(FboListView):
    def get_context_data(self, **kwargs):
        context = super(FboMagicView, self).get_context_data(**kwargs)
        return context

    def get_table_data(self):
        naics_list = self.request.user.userprofile.account.sam.naics.split()
        return super(FboMagicView, self).get_table_data().filter(naics__in=naics_list)

def FboAddView(request, pk):

    # Get the information necessary to create a new opportunity

    opportunityFboMaster = FboMaster.objects.get(pk=pk)
    opportunityOwner = request.user.userprofile

    # Create the new opportunity

    newOpportunity = Opportunity.objects.create(fbo_master=opportunityFboMaster, owner=opportunityOwner)

    # Add contacts to the users's watchlist

    userprofile = request.user.userprofile
    for contact in opportunityFboMaster.contacts.all():
        contact.related_users.add(userprofile)

    # Go to the new opportunity record

    return HttpResponseRedirect(reverse('opportunity:detail', kwargs={'pk':newOpportunity.id}))

