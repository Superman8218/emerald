import django_tables2 as tables
from django_tables2.utils import A

from models import FboMaster

class FboMasterTable(tables.Table):
    class Meta:
        model = FboMaster
        attrs = {'class':'table'}
        exclude = ('id', 'subject', )
        sequence = ('solnbr', 'description', '...')

    solnbr = tables.LinkColumn('fbo:detail', args=[A('pk')])
