from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from sam.models import SamRecord

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    sam = models.ForeignKey(SamRecord, null=True, blank=True)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def handle_new_user(sender, instance, created, **kwargs):

        # Set up a new record

        if created:

            # Set up a User Profile

            newProfile = UserProfile()
            newProfile.user = instance

            # Save the new object

            newProfile.save()

    def __unicode__(self):
        return u'{0}'.format(self.user.get_full_name())
