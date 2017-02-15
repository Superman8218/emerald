import django_tables2 as tables
from django_tables2.utils import A

from models import FboMaster

class FboMasterTable(tables.Table):
    class Meta:
        model = FboMaster
        attrs = {'class':'table'}
        exclude = ('id', 'subject', )
        sequence = ('add_button', 'solnbr', 'description', '...')

    add_button = tables.TemplateColumn(verbose_name='Watch',
                                       template_name='fbo/btn-watch.html')
    solnbr = tables.LinkColumn('fbo:detail', args=[A('pk')])

    offset = 1

