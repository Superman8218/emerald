import django_tables2 as tables

from models import Contact

class ContactTable(tables.Table):
    class Meta:
        model = Contact
        attrs = {'class':'table'}
