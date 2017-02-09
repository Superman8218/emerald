from django_filters import FilterSet

from models import Contact

class ContactFilter(FilterSet):
    class Meta:
        model = Contact
        fields = '__all__'
