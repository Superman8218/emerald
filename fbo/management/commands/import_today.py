from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from fbo.fbo_import import FboImporter
import pdb


class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        # try:
            # FboImporter.process_single_date(datetime.today())
        # except:
            # raise CommandError('Fbo import failed')
        importer = FboImporter()
        pdb.set_trace()
        import_dt = datetime.today() + timedelta(days=-2)
        importer.process_single_date(import_dt)

        self.stdout.write('Fbo import successful')
