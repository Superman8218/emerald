from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from sam.models import SamRecord

import pdb

# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=150, default="New Account")
    sam = models.OneToOneField(SamRecord, null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    account = models.ForeignKey(Account)

    @receiver(post_save, sender=User)
    def handle_new_user(sender, instance, created, **kwargs):

        # Set up a new record

        if created:

            # Set up a User Profile

            newProfile = UserProfile()
            newProfile.user = instance

            # Set account to either given Account or a new Account

            if False: # NOT FULLY IMPLEMENTED
                pass

            else:
                accountName = " ".join([instance.first_name, instance.last_name, "Account"])
                newProfile.account = Account.objects.create(name=accountName)

            #Finally save the new object

            newProfile.save()
