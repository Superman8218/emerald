from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import View, DetailView, ListView

from emerald.views import FilteredSingleTableView
from filters import ContactFilter
from forms import ContactFilterFormHelper
from models import Contact
from tables import ContactTable
from userprofile.models import UserProfile

class ContactDetailView(LoginRequiredMixin, DetailView):

    model = Contact
    template_name = 'contact/contact-detail.html'

class ContactListView(FilteredSingleTableView, LoginRequiredMixin, ListView):

    model = Contact
    template_name = 'contact/contact-list.html'
    table_class = ContactTable
    filter_class = ContactFilter
    helper_class = ContactFilterFormHelper

    def get_queryset(self):
        return Contact.objects.filter(related_users__id=self.request.user.userprofile.id)
