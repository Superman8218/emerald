from django.db import models

class FboMasterManager(models.Manager):

    def get_by_account(self, account):
        return super(FboMasterManager, self).get_queryset().filter(account=account)
