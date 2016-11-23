from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from fbo.fbo_import import FboImporter


class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        # try:
            # FboImporter.process_single_date(datetime.today())
        # except:
            # raise CommandError('Fbo import failed')
        FboImporter.process_single_date(datetime.today())

        self.stdout.write('Fbo import successful')
