from datetime import datetime
import os.path
import zipfile

from importer.models import Importer
from parser import parse_file


class SAMImporter(Importer):

    # Implement Importer methods
    base_url = 'https://www.sam.gov/SAMPortal/extractfiledownload?role=WW&version=SAM&filename=SAM_PUBLIC_DAILY_{0}.ZIP'
    url_date_format = '%Y%m%d'
    storage_dir = 'sam/sam_files'
    base_file_name = 'SAM_PUBLIC_DAILY_{0}'
    initial_file_dt = datetime(2016, 11, 21)
    data_source = 'sam'

    def process_file(self, file_path):
        # Unzip the file

        zip_ref = zipfile.ZipFile(file_path, 'r')
        zip_ref.extractall(os.path.dirname(file_path))
        zip_ref.close()
        csv_path =  os.path.join(os.path.dirname(file_path), os.path.basename(file_path)) + '.dat'

        #Process the file

        parse_file(csv_path)
        os.remove(csv_path)

        return True

    # Helper methods for processing the file
