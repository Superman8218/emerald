import datetime

from django.db import models

from accounts.models import Account
from contact.models import Contact
import choices
from managers import FboMasterManager 

class FboMaster(models.Model):

    solicitation_type = models.CharField(max_length=20, choices=choices.SOLICITATION_TYPES)
    date = models.DateField(null=True)
    zip_code = models.CharField(max_length=30, null=True) #zip
    class_code = models.CharField(max_length=10, null=True) #classcod
    naics = models.CharField(max_length=10, null=True)
    office_address = models.CharField(max_length=400, null=True) #offadd
    subject = models.CharField(max_length=400, null=True)
    solnbr = models.CharField(max_length=100, null=True)
    response_date = models.DateField(null=True) #respdate
    archive_date = models.DateField(null=True) #archdate
    contacts = models.ManyToManyField(Contact) #contact
    description = models.TextField() #desc
    link = models.URLField(null=True)
    email = models.EmailField(null=True)
    # links - array of links to documents
    # files - array of files
    agency = models.CharField(max_length=200, null=True)
    office = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    url = models.URLField()
    setaside = models.CharField(max_length=100, null=True)
    pop_country = models.CharField(max_length=50, null=True)
    pop_address = models.CharField(max_length=100, null=True)
    pop_zip = models.CharField(max_length=30, null=True)
    award_number = models.CharField(max_length=30, null=True)
    award_amount = models.IntegerField(null=True)
    award_date = models.DateField(null=True)
    line_number = models.CharField(max_length=30, null=True)
    ntype = models.CharField(max_length=30, null=True)


    objects = FboMasterManager()

    class Meta:

        verbose_name = 'solicitation'
        verbose_name_plural = 'solicitations'

    def __unicode__(self):

        return self.description
