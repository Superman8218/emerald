from django.core.management.base import BaseCommand, CommandError

from sam.parser import parse_file

import os
import pdb


class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        # try:
            # FboImporter.process_single_date(datetime.today())
        # except:
            # raise CommandError('Fbo import failed')
        parse_file('sam/sam_files/SAM_PUBLIC_DAILY_20161105.dat')
        self.stdout.write('Sam import successful')
