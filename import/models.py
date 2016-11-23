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

    objects = ImportHistoryManager()

class Importer():

    model = None

    def get_base_url():
        """Returns the base url for the import in a string ready to be formatted with the correct date"""
        raise NotImplementedError

    def get_url_date_format():
        """Returns a string that specifies the format to be used when inserting the date into the url"""
        raise NotImplementedError

    def get_storage_dir():
        """Returns a path to the directory where we will store the import file"""
        raise NotImplementedError

    def get_base_file_name():
        """Returns the root a the file name for the imported file, ready to be formatted with a date"""
        raise NotImplementedError

    def process_file(file_path):
        """Processing a single file"""
        raise NotImplementedError

    def get_initial_file_dt():
        """Returns the first day from which we should be getting records"""


def do_import():
    import_model = model()
    last_successful_dt = import_model.objects.last_successful_dt()
    next_file_dt = None
    if last_successful_dt == None:
       next_file_dt = import_model.get_initial_file_dt()
    else:
        next_file_dt = last_successful_dt + timedelta(days=1)

    while next_file_dt < (datetime.now() + timedelta(days=1)):
        # Download the file for the given date, process it, and then create a record of the import

        file_path = download_file(import_model, next_file_dt)
        success = import_model.process_file(file_path)
        ImportHistory.objects.record_import(next_file_dt, success)
        next_file_dt = next_file_dt + timedelta(days=1)

def download_file(import_model, file_dt):
    date_parameter = file_dt.strftime(import_model.get_url_date_format)
    storage_dir = import_model.get_storage_dir()
    file_name = import_model.get_base_file_name.format(date_parameter)
    file_path = os.join(storage_dir, file_name)
    file_url = import_model.get_base_url.format(date_parameter)
    response = urllib2.urlopen(url)

    text_file = open(file_path, 'w')
    text_file.write(response.read())
    text_file.close()

    return file_path
