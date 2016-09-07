from django.conf.urls import url

from views import FboDetailView, FboImportView, FboListView

urlpatterns = [
        url(r'^fbo/(?P<pk>[0-9]*)/$', FboDetailView.as_view()),
        url(r'^import/$', FboImportView),
        url(r'^fbo/list/$', FboListView.as_view())
]
