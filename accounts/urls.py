from django.conf.urls import url

from views import register, LoginView, logout_view

urlpatterns = [
        url(r'^register/$', register),
        url(r'login/$', LoginView.as_view(), name='login'),
        url(r'logout/$', logout_view, name='logout')
]
