from django.core.management.base import BaseCommand, CommandError
from data import fbo_import

class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        try:
            fbo_import.main()
        except:
            raise CommandError('Fbo import failed')
        
        self.stdout.write('Fbo import successful')
