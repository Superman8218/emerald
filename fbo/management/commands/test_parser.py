from django.core.management.base import BaseCommand, CommandError

from fbo.parser import parse_file

from contact.models import Contact
from fbo.models import FboMaster
import os
import pdb


class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        # try:
            # FboImporter.process_single_date(datetime.today())
        # except:
            # raise CommandError('Fbo import failed')
        FboMaster.objects.all().delete()
        Contact.objects.all().delete()
        parse_file('fbo/fbo_files/test.fbo')
        self.stdout.write('Fbo import successful')
