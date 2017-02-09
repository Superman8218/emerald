from django.conf.urls import url

from models import Opportunity
from views import OpportunityDetailView, OpportunityListView

urlpatterns = [
        url(r'^(?P<pk>[0-9]*)/$', OpportunityDetailView.as_view(), name='detail'),
        url(r'^list/$', OpportunityListView.as_view(), name='list'),
]
