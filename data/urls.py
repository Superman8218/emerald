from django.conf.urls import url

from views import FboDetailView, FboImportView, FboListView, OpportunityDetailView, OpportunityListView

urlpatterns = [
        url(r'^fbo/(?P<pk>[0-9]*)/$', FboDetailView.as_view()),
        url(r'^import/$', FboImportView),
        url(r'^fbo/list/$', FboListView.as_view()),
        url(r'^opportunity/detail/(?P<pk>[0-9]*)/$', OpportunityDetailView.as_view()),
        url(r'^opportunity/list', OpportunityListView.as_view())
]
