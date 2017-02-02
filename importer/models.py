from __future__ import unicode_literals

from datetime import datetime, timedelta
from exceptions import NotImplementedError
import logging
import os
import pytz
import urllib2

from django.db import models
from django.utils import timezone

from managers import ImportHistoryManager

import pdb

logger = logging.getLogger(__name__)

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

    # This is a method that can be overridden if necessary so that we can get different url formattings. The default version only works when there is one date that needs to go in.

    def format_base_url(self, file_dt):
        formatted_date = file_dt.strftime(self.url_date_format)
        return self.base_url.format(formatted_date)

    def process_file(self, file_path):
        """Processing a single file"""
        raise NotImplementedError

    # The methods for actually doing the import

    def do_import(self):
        """Runs the whole import"""


        # Make sure storage_dir exists
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

        last_successful_dt = ImportHistory.objects.last_successful_dt(self.data_source)
        next_file_dt_naive = None
        if last_successful_dt == None:
           next_file_dt_naive = self.initial_file_dt
        else:
            next_file_dt_naive = last_successful_dt + timedelta(days=1)

        if next_file_dt_naive.tzinfo is None:
            next_file_dt = pytz.utc.localize(next_file_dt_naive)
        else:
            next_file_dt = next_file_dt_naive

        while next_file_dt < (timezone.now() + timedelta(days=1)):
            try:
                self.process_single_date(next_file_dt)
            except Exception, err:
                logger.error('Unable to process file date: {0}, {1}'.format(self.data_source, next_file_dt.strftime(self.url_date_format)))
            next_file_dt = next_file_dt + timedelta(days=1)

    def download_file(self, file_dt):
        """Download a given file so that for processing"""
        date_parameter = file_dt.strftime(self.url_date_format)
        file_name = self.base_file_name.format(date_parameter).replace('/', '')
        file_path = os.path.join(self.storage_dir, file_name)
        file_url = self.format_base_url(file_dt)
        try:
            response = urllib2.urlopen(file_url)
        except urllib2.HTTPError, err:
            logger.info('Download failed for url: {0}'.format(file_url))
        # pdb.set_trace()
        text_file = open(file_path, 'w')
        text_file.write(response.read())
        text_file.close()
        response.close()

        return file_path

    def process_single_date(self, file_dt):
        """Download the file for the given date, process it, and then create a record of the import"""
        if file_dt.tzinfo is None or file_dt.tzinfo.utcoffset(file_dt) is None:
            file_dt = pytz.utc.localize(file_dt)
        # pdb.set_trace()
        file_path = self.download_file(file_dt)
        success = self.process_file(file_path)
        os.remove(file_path)
        ImportHistory.objects.record_import(self.data_source, file_dt, success)
