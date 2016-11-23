from django.core.management.base import BaseCommand, CommandError
from sam import sam_import

class Command(BaseCommand):
    help = 'Runs the Sam Import task'

    def handle(self, *args, **options):
        try:
            sam_import.main()
        except:
            raise CommandError('Sam import failed')

        self.stdout.write('Sam import successful')
