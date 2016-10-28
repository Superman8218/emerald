from django_filters import FilterSet

from models import FboMaster

class FboMasterFilter(FilterSet):
    class Meta:
        model = FboMaster
        fields = '__all__'
