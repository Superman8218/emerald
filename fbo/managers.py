from django.db import models

from models import FboMaster

class FboMasterManager(models.Manager):

    def magic_qs(self, request):
        cage_code = request.user.cage_code
        return super(FboMasterManager, self).get_queryset().filter(class
