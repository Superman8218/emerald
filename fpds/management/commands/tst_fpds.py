from django.core.management.base import BaseCommand, CommandError

from fpds.parser import parse_file

import os
import pdb


class Command(BaseCommand):
    help = 'Runs the FPDS Import task'

    def handle(self, *args, **options):
        parse_file('fpds/fpds_files/FPDS_ATOM_FEED_20161105')
        self.stdout.write('Fpds import successful')
