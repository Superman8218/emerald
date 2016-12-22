from datetime import datetime, timedelta

from importer.models import Importer
from parser import parse_file

class FPDSImporter(Importer):
    
    base_url = 'https://www.fpds.gov/ezsearch/FEEDS/ATOM?FEEDNAME=PUBLIC&q=LAST_MODIFIED_DATE:[{0},{1}]'
    url_date_format = '%Y/%m/%d'
    storage_dir = 'fpds/fpds_files'
    base_file_name = 'FPDS_ATOM_FEED_{0}'
    initial_file_dt = datetime(2016, 1, 1)
    data_source = 'fpds'

    def format_base_url(self, file_dt):
        first_date = (file_dt + timedelta(days=-1)).strftime(self.url_date_format)
        second_date = file_dt.strftime(self.url_date_format)
        return self.base_url.format(first_date, second_date)

    def process_file(self, file_path):
        parse_file(file_path)
        return True
