from __future__ import unicode_literals

from django.db import models

from userprofile.models import UserProfile

class Contact(models.Model):

    name = models.CharField(max_length=60)
    title = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=20, null=True)
    fax = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)

    related_users = models.ManyToManyField(UserProfile, related_name='related_users')

    def __unicode__(self):
        return self.name
