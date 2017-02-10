import django_tables2 as tables
from django_tables2.utils import A

from models import Contact

class ContactTable(tables.Table):
    class Meta:
        model = Contact
        attrs = {'class':'table'}
        exclude = ('id', )
        sequence = ('name', '...')

    name = tables.LinkColumn('contact:detail', args=[A('pk')])
