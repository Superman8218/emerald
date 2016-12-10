from django.core.management.base import BaseCommand, CommandError
from sam.sam_import import SAMImporter
import traceback

class Command(BaseCommand):
    help = 'Runs the Sam Import task'

    def handle(self, *args, **options):
        try:
            importer = SAMImporter()
            importer.do_import()
        except Exception, e:
            traceback.print_exc()
            raise CommandError('Sam import failed')

        self.stdout.write('Sam import successful')
