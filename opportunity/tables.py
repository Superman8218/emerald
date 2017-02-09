import django_tables2 as tables
from django_tables2.utils import A

from models import Opportunity

class OpportunityTable(tables.Table):
    class Meta:
        model = Opportunity
        attrs = {'class':'table'}

    id = tables.LinkColumn('opportunity:detail', args=[A('pk')])
