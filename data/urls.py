from django.conf.urls import url

from views import detail

urlpatterns = [
        url(r'^detail', detail)
]
