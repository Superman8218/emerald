from django.db import models

class OpportunityManager(models.Manager):

    def get_by_owner(self, owner):
        return super(OpportunityManager, self).get_queryset().filter(owner=owner)
