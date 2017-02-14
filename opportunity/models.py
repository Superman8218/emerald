from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from fbo.models import FboMaster
from managers import OpportunityManager
from userprofile.models import UserProfile

class Opportunity(models.Model):

    fbo_master = models.ForeignKey(FboMaster, related_name='fbo_master')
    owner = models.ForeignKey(UserProfile)

    objects = OpportunityManager()

    class Meta:

        verbose_name_plural = "opportunities"

    def __unicode__(self):
        return self.fbo_master.description
