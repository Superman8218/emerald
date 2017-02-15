import django_tables2 as tables
from django_tables2.utils import A

from models import Opportunity

class OpportunityTable(tables.Table):
    class Meta:
        model = Opportunity
        attrs = {'class':'table'}
        exclude = ('id', 'fbo_master', 'owner', )
        sequence = ('remove_button', 'solnbr', 'description', '...')

    id = tables.LinkColumn('opportunity:detail', args=[A('pk')])

    solnbr = tables.Column(accessor = A('fbo_master.solnbr'))
    description = tables.Column(accessor=A('fbo_master.description'))
    remove_button = tables.TemplateColumn(verbose_name=('Remove'),
                                          template_name='opportunity/btn-remove.html')

    offset = 1

