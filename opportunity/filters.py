import django_filters

from emerald.filters import StartsWithCharFilter
from models import Opportunity

class OpportunityFilter(django_filters.FilterSet):
    class Meta:
        model = Opportunity
        offset = 1
        # fields = '__all__'

    solnbr = StartsWithCharFilter(name='fbo_master__solnbr')
    description = StartsWithCharFilter(name='fbo_master__description')
