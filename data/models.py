from __future__ import unicode_literals

from django.db import models

import choices

# Create your models here.

class FboMaster(models.Model):

    solicitation_type = models.CharField(max_length=20, choices=choices.SOLICITATION_TYPES)
    date = models.CharField(max_length=4)
    year = models.CharField(max_length=4)
    agency = models.CharField(max_length=80)
    office = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=15)
    class_code = models.CharField(max_length=10)
    naics = models.CharField(max_length=10)
    office_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=200)
    solnbr = models.CharField(max_length=20)
    response_date = models.DateField(null=True)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=15)
    contact_email = models.EmailField()
    description = models.TextField()
    url = models.URLField()
    setaside = models.CharField(max_length=15)
    pop_country = models.CharField(max_length=50)
    pop_address = models.CharField(max_length=100)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in FboMaster._meta.fields]
