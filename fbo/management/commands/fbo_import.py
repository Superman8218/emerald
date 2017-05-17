from django.core.management.base import BaseCommand, CommandError

from fbo import fbo_import
from fbo.fbo_import import FboImporter
import pdb

class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        try:
            importer = FboImporter()
            importer.do_import()
        except:
            raise CommandError('Fbo import failed')

        self.stdout.write('Fbo import successful')
