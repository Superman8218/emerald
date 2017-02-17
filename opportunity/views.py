from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import DeleteView

from emerald.views import FilteredSingleTableView
from filters import OpportunityFilter
from forms import OpportunityFilterFormHelper
from models import Opportunity
from tables import OpportunityTable

class OpportunityDetailView(LoginRequiredMixin, DetailView):

    model = Opportunity
    template_name = 'opportunity/opportunity-detail.html'

class OpportunityListView(FilteredSingleTableView, LoginRequiredMixin, ListView):

    model = Opportunity
    template_name = 'opportunity/opportunity-list.html'
    table_class = OpportunityTable
    filter_class = OpportunityFilter
    helper_class = OpportunityFilterFormHelper

    # Only list the opportunites that belong to the logged in user's account

    def get_queryset(self):
        return Opportunity.objects.filter(owner=self.request.user.userprofile)

class OpportunityDeleteView(LoginRequiredMixin, DeleteView):

    model = Opportunity
    success_url = reverse_lazy('opportunity:list')

def OpportunityAddView(request, pk):
    '''Takes an opportunity and sets its pipeline stage to be 1, the first stage in the pipeline'''

    opportunity = Opportunity.objects.get(pk=pk)
    opportunity.increment_pipeline_stage()
    opportunity.save()

    return HttpResponseRedirect(reverse_lazy('pipeline:detail', request.user.userprofile.default_pipeline.pk))
