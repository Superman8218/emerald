from __future__ import unicode_literals

from django.db import models

from userprofile.models import UserProfile

class Pipeline(models.Model):
    userprofile = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return u'{0}\'s Pipeline'.format(self.userprofile.user.get_full_name())
    pass

class PipelineStage(models.Model):

    pipeline = models.ForeignKey(Pipeline)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)
