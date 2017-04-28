from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin

from emerald.views import index
from emerald.views import landing
from emerald.views import thanks

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^/', landing, name='landing'),
        url(r'^thanks', thanks, name='thanks'),
]
