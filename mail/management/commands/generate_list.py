from django.core.management.base import BaseCommand, CommandError

from mail.generate_list import generate_email_csv

class Command(BaseCommand):
    help = 'Generate a list of emails'

    def handle(self, *args, **options):
        try:
            generate_email_csv()
        except Exception as e:
            self.stdout.write(str(e))
            raise CommandError('Email List Generation Failed')
        self.stdout.write('Email List Generated')
