from __future__ import unicode_literals

from django.db import models

class SamRecord(models.Model):

    duns = models.IntegerField()
    cage_code = models.CharField(max_length=4)
    registration_purpose = models.CharField(max_length=2)
    company_nm = models.CharField(max_length=120)
    primary_naics = models.CharField(max_length=6)
    naics_codes = models.CharField(max_length=12000)
    email_address = models.EmailField(max_length=80)
    is_sdb = models.BooleanField(default=False)
    is_8a = models.BooleanField(default=False)
    is_hubzone = models.BooleanField(default=False)
