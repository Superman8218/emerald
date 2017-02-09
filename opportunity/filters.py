from django_filters import FilterSet

from models import Opportunity

class OpportunityFilter(FilterSet):
    class Meta:
        model = Opportunity
        fields = '__all__'
