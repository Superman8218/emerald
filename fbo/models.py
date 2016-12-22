from __future__ import unicode_literals

import datetime

from django.db import models

from accounts.models import Account
import choices


class FboMaster(models.Model):

    solicitation_type = models.CharField(max_length=20, choices=choices.SOLICITATION_TYPES)
    # date = models.CharField(max_length=4)
    # year = models.CharField(max_length=4)
    date = models.DateField(null=True)
    agency = models.CharField(max_length=200)
    office = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=30)
    class_code = models.CharField(max_length=10)
    naics = models.CharField(max_length=10)
    office_address = models.CharField(max_length=400)
    subject = models.CharField(max_length=400)
    solnbr = models.CharField(max_length=100)
    response_date = models.DateField(null=True)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=30)
    contact_email = models.EmailField()
    description = models.TextField()
    url = models.URLField()
    setaside = models.CharField(max_length=100)
    pop_country = models.CharField(max_length=50)
    pop_address = models.CharField(max_length=100)

class Opportunity(models.Model):
    fbomaster = models.ForeignKey(FboMaster)
    account = models.ForeignKey(Account)
