from django.core.management.base import BaseCommand, CommandError
from data import FboImport

class Command(BaseCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, *args, **options):
        try:
            FboImport.main()
        except:
            raise CommandError('Fbo import failed')
        
        self.stdout.write('Fbo import successful')
