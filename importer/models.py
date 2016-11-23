from __future__ import unicode_literals

from datetime import datetime, timedelta
from exceptions import NotImplementedError
import os
import urllib2

from django.db import models

from managers import ImportHistoryManager


class ImportHistory(models.Model):

    file_dt = models.DateTimeField()
    success = models.BooleanField()
    data_source = models.CharField(max_length=10)

    objects = ImportHistoryManager()

class Importer():

    # These are the parts that should be overridden

    base_url = None
    url_date_format = None
    storage_dir = None
    base_file_name = None
    initial_file_dt = None
    data_source = None

    def process_file(file_path):
        """Processing a single file"""
        raise NotImplementedError

    # The methods for actually doing the import

    def do_import():
        last_successful_dt = ImportHistory.objects.last_successful_dt(self.data_source)
        next_file_dt = None
        if last_successful_dt == None:
           next_file_dt = self.initial_file_dt()
        else:
            next_file_dt = last_successful_dt + timedelta(days=1)

        while next_file_dt < (datetime.now() + timedelta(days=1)):
            process_single_date(next_file_dt)
            next_file_dt = next_file_dt + timedelta(days=1)



    def download_file(file_dt):
        """Download a given file so that for processing"""
        date_parameter = file_dt.strftime(self.url_date_format)

        # Make sure storage_dir exists
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

        file_name = self.base_file_name.format(date_parameter)
        file_path = os.join(self.storage_dir, file_name)
        file_url = import_model.get_base_url.format(date_parameter)
        response = urllib2.urlopen(url)

        text_file = open(file_path, 'w')
        text_file.write(response.read())
        text_file.close()

        return file_path


    def process_single_date(file_dt):
        """Download the file for the given date, process it, and then create a record of the import"""
        file_path = download_file(next_file_dt)
        success = self.process_file(file_path)
        os.remove(file_path)
        ImportHistory.objects.record_import(next_file_dt, data_source, success)
