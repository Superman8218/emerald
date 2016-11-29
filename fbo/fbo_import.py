from django.utils import timezone
from datetime import datetime
import pytz

from importer.models import Importer


class FboImporter(Importer):

    # Implement Importer methods
    base_url = 'ftp://ftp.fbo.gov//FBOFeed{0}'
    url_date_format = '%Y%m%d'
    storage_dir = 'fbo/fbo_files'
    base_file_name = 'fbo_daily_file{0}'
    initial_file_dt = datetime(2016, 11, 21)
    data_source = 'fbo'

    def process_file(self, file_path):
        print 'File Processed'
        return True

    # Helper methods for processing the file
