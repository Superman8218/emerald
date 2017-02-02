from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):

    name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=40, null=True)
    phone = models.CharField(max_length=18, null=True)
    fax = models.CharField(max_length=18, null=True)
    email = models.EmailField(null=True)
