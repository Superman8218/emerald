from datetime import datetime

from importer.models import Importer


class FboImporter(Importer):

    # Implement Importer methods
    def get_base_url():
        return 'ftp://ftp.fbo.gov//FBOFeed{0}'

    def get_url_date_format():
        return '%Y%m%d'

    def get_storage_dir():
        return 'fbo/fbo_files'

    def get_base_file_name():
        return 'fbo_daily_file{0}'

    def get_initial_file_dt():
        return datetime.date(2016,1,1)

    def get_data_source_nm():
        return 'fbo'

    def processFile(file_path):
        print 'File Processed'

    # Helper methods for processing the file
