from django.db import models

import pdb

class FboMasterManager(models.Manager):

    # def magic(self, request):
        # naics_list = request.user.userprofile.account.sam.naics.split()
        # return super(FboMasterManager, self).get_queryset().filter(naics__in=naics_list)

    def get_by_account(self, account):
        return super(FboMasterManager, self).get_queryset().filter(account=account)
