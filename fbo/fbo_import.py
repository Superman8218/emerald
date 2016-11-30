from datetime import datetime

from importer.models import Importer
from parser import parse_file


class FboImporter(Importer):

    # Implement Importer methods
    base_url = 'ftp://ftp.fbo.gov//FBOFeed{0}'
    url_date_format = '%Y%m%d'
    storage_dir = 'fbo/fbo_files'
    base_file_name = 'fbo_daily_file{0}'
    initial_file_dt = datetime(2016, 11, 21)
    data_source = 'fbo'

    def process_file(self, file_path):
        parse_file(file_path)
        return True

    # Helper methods for processing the file
