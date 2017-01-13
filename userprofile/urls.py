from django.conf.urls import url

from views import UserProfileUpdateView

urlpatterns = [
        url(r'update/(?P<pk>[0-9]+)/$', UserProfileUpdateView, name='update'),
]
