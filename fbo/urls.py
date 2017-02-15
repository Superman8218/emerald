from django.conf.urls import url

from models import FboMaster

from views import FboDetailView, FboListView, FboMagicView, FboAddView

urlpatterns = [
        url(r'^(?P<pk>[0-9]*)/$', FboDetailView.as_view(), name='detail'),
        url(r'^list/$', FboListView.as_view(), name='list'),
        url(r'^magic/$', FboMagicView.as_view(), name='magic'),
        url(r'^add/(?P<pk>[0-9]*)/$', FboAddView, name='add'),
]
