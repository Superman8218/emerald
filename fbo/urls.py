from django.conf.urls import url

from models import FboMaster

from views import FboDetailView, FboListView, FboMagicView, FboAddView, OpportunityDetailView, OpportunityListView

urlpatterns = [
        url(r'^(?P<pk>[0-9]*)/$', FboDetailView.as_view(), name='detail'),
        url(r'^list/$', FboListView.as_view(), name='list'),
        url(r'^magic/$', FboMagicView.as_view(), name='magic'),
        url(r'^(?P<pk>[0-9]*)/add/$', FboAddView, name='add'),
 #        url(r'^opportunity/detail/(?P<pk>[0-9]*)/$', OpportunityDetailView.as_view(), name='opportunity-detail'),
 #        url(r'^opportunity/list', OpportunityListView.as_view(), name='opportunity-list')
]
