"""emerald URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin

from emerald.views import index
from emerald.views import landing
from emerald.views import thanks

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', index, name='home'),
        url(r'^landing', landing, name='landing'),
        url(r'^thanks', thanks, name='thanks'),
        url(r'^accounts/', include('accounts.urls', namespace='accounts')),
        url(r'^contact/', include('contact.urls', namespace='contact')),
        url(r'^fbo/', include('fbo.urls', namespace='fbo')),
        url(r'^opportunity/', include('opportunity.urls', namespace='opportunity')),
        url(r'^userprofile/', include('userprofile.urls', namespace='userprofile')),
        url(r'^pipeline/', include('pipeline.urls', namespace='pipeline')),
]
