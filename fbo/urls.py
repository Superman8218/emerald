from django.conf.urls import url

from models import FboMaster

from views import FboDetailView, FboImportView, FboListView, FboAddView, OpportunityDetailView, OpportunityListView

urlpatterns = [
        url(r'^fbo/(?P<pk>[0-9]*)/$', FboDetailView.as_view(), name='fbo-detail'),
        url(r'^fbo/list/$', FboListView.as_view(), name='fbo-list'),
        url(r'^import/$', FboImportView, name='fbo-import'),
        url(r'^fbo/(?P<pk>[0-9]*)/add/$', FboAddView, name='fbo-add'),
        url(r'^opportunity/detail/(?P<pk>[0-9]*)/$', OpportunityDetailView.as_view(), name='opportunity-detail'),
        url(r'^opportunity/list', OpportunityListView.as_view(), name='opportunity-list')
]
