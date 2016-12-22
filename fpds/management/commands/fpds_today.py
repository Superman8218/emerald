import datetime
from datetime import timedelta
import pytz

from django.core.management.base import BaseCommand, CommandError

from fpds.fpds_import import FPDSImporter
import pdb


class Command(BaseCommand):
    help = 'Runs the FPDS Import task'

    def handle(self, *args, **options):
        importer = FPDSImporter()
        import_dt = datetime.datetime(2016, 11, 5) #+ timedelta(days=-4)
        importer.process_single_date(import_dt)

        self.stdout.write('FPDS single day import successful')
