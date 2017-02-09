import django_tables2 as tables

from models import FboMaster

class FboMasterTable(tables.Table):
    class Meta:
        model = FboMaster
        attrs = {'class':'table'}
        exclude = ('id', 'subject', )
