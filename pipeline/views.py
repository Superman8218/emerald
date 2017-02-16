from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, ListView, TemplateView
from django.views.generic.edit import DeleteView

from models import Pipeline

class PipelineDetailView(LoginRequiredMixin, DetailView):

    model = Pipeline
    template_name = 'pipeline/pipeline-detail.html'

def PipelineDefaultNewView(request):

    new_pipeline = Pipeline()
    new_pipeline.userprofile = request.user.userprofile
    new_pipeline.save()

    return HttpResponseRedirect(reverse_lazy('pipeline:detail', kwargs={'pk': new_pipeline.pk}))

class PipelineManageView(TemplateView):

    template_name = 'pipeline/pipeline-manage.html'

    def get_context_data(self, **kwargs):

         context = super(PipelineManageView, self).get_context_data(**kwargs)

         # Add the current user's information to the request
         context['pipeline'] = self.request.user.userprofile.default_pipeline
         context['stages'] = self.request.user.userprofile.default_pipeline.pipelinestage_set.all()
         return context
