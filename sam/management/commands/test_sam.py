from django.core.management.base import BaseCommand, CommandError

from sam.parser import parse_file
from sam.models import SamRecord

import os
import pdb


class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        # try:
            # FboImporter.process_single_date(datetime.today())
        # except:
            # raise CommandError('Fbo import failed')
        SamRecord.objects.all().delete()
        parse_file('sam/sam_files/SAM_PUBLIC_DAILY_20161105.dat')
        self.stdout.write('Sam import successful')
