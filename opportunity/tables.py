import django_tables2 as tables
from django_tables2.utils import A

from models import Opportunity

class OpportunityTable(tables.Table):
    class Meta:
        model = Opportunity
        attrs = {'class':'table'}
        exclude = ('id', 'fbo_master', )
        sequence = ('solnbr', 'description', 'owner', '...')

    id = tables.LinkColumn('opportunity:detail', args=[A('pk')])

    solnbr = tables.Column(accessor = A('fbo_master.solnbr'))
    description = tables.Column(accessor=A('fbo_master.description'))
