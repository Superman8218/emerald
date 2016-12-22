from datetime import datetime, timedelta

from django.core.management.base import BaseCommand, CommandError

from sam.sam_import import SAMImporter


class Command(BaseCommand):
    help = 'Runs the Sam Import task'

    def handle(self, *args, **options):
        importer = SAMImporter()
        import_dt = datetime.date(2016, 11, 5) #+ timedelta(days=-4)
        importer.process_single_date(import_dt)

        self.stdout.write('SAM single day import successful')
