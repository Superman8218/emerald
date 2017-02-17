from django.conf.urls import url

from models import Opportunity
from views import OpportunityDetailView, OpportunityListView, OpportunityDeleteView, OpportunityAddView

urlpatterns = [
        url(r'^(?P<pk>[0-9]*)/$', OpportunityDetailView.as_view(), name='detail'),
        url(r'^list/$', OpportunityListView.as_view(), name='list'),
        url(r'^delete/(?P<pk>[0-9]+)/$', OpportunityDeleteView.as_view(), name='delete'),
        url(r'^add/(?P<pk>[0-9]+)/$', OpportunityAddView, name='add'),
]
