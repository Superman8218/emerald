from django.core.management.base import NoArgsCommand, CommandError
from data import FboImport

class Command(NoArgsCommand):
    help = 'Runs the Fbo Import task'

    def handle(self, **options):
        try:
            FboImport.main()
        except:
            raise CommandError('Fbo import failed')
        
        self.stdout.write('Fbo import successful')
