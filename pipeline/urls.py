from django.conf.urls import url

from models import Pipeline
from views import PipelineDetailView, PipelineDefaultNewView, PipelineManageView

urlpatterns = [
        url(r'^default-new/$', PipelineDefaultNewView, name='default-new'),
        url(r'^(?P<pk>[0-9]+)/$', PipelineDetailView.as_view(), name='detail'),
        url(r'^manage/$', PipelineManageView.as_view(), name='manage'),
]
