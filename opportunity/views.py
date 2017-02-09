from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, ListView

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
