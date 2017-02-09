import datetime

from django.db import models

from accounts.models import Account
from contact.models import Contact
import choices
from managers import FboMasterManager


class FboMaster(models.Model):

    solicitation_type = models.CharField(max_length=20, choices=choices.SOLICITATION_TYPES)
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
    contacts = models.ManyToManyField(Contact)
    description = models.TextField()
    url = models.URLField()
    setaside = models.CharField(max_length=100)
    pop_country = models.CharField(max_length=50)
    pop_address = models.CharField(max_length=100)

    objects = FboMasterManager()

    class Meta:

        verbose_name = 'solicitation'
        verbose_name_plural = 'solicitations'
