from datetime import datetime

from importer.models import Importer
from parser import parse_file


class SAMImporter(Importer):

    # Implement Importer methods
    base_url = 'https://www.sam.gov/SAMPortal/extractfiledownload?role=WW&version=SAM&filename=SAM_PUBLIC_DAILY{0}.ZIP'
    url_date_format = '%Y%m%d'
    storage_dir = 'sam/sam_files'
    base_file_name = 'sam_daily_file{0}'
    initial_file_dt = datetime(2016, 11, 21)
    data_source = 'sam'

    def process_file(self, file_path):
        parse_file(file_path)
        return True

    # Helper methods for processing the file
