from django.conf.urls import url

from models import Contact
from views import ContactDetailView, ContactListView

urlpatterns = [
        url(r'^(?P<pk>[0-9]*)/$', ContactDetailView.as_view(), name='detail'),
        url(r'^list/$', ContactListView.as_view(), name='list'),
]
