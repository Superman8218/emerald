from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from fbo.models import FboMaster
from managers import OpportunityManager
from pipeline.models import PipelineStage
from userprofile.models import UserProfile

class Opportunity(models.Model):

    fbo_master = models.ForeignKey(FboMaster, related_name='fbo_master')
    owner = models.ForeignKey(UserProfile)
    pipeline_stage = models.ForeignKey(PipelineStage, null=True)

    objects = OpportunityManager()

    class Meta:

        verbose_name_plural = "opportunities"

    def __unicode__(self):
        return self.fbo_master.description

    def change_pipeline_stage(self, change_number):

        if self.pipeline_stage:
            current_stage_number = self.pipeline_stage.stage_number
            current_stage_pipeline = self.pipeline_stage.pipeline

        else:
            current_stage_number = 0
            current_stage_pipeline = self.owner.default_pipeline

        if len(current_stage_pipeline.pipeline_set.all()) == 0:
            raise Exception('Your pipeline has not been set up yet')

        new_stage_number = current_stage_number + change_number

        if new_stage_number < 0 or new_stage_number >= len(current_stage_pipeline.pipelinestage_set.all()):
            raise IndexError('The new stage number doesn\'t fall within the given pipeline\s number of stages')

        self.pipeline_stage = PipelineStage.objects.get(stage_number=new_stage_number, pipeline=current_stage_pipeline)

        self.save()

    def increment_pipeline_stage(self):

        self.change_pipeline_stage(1)

    def decrement_pipeline_stage(self):

        self.change_pipeline_stage(-1)
