from django.db import models
from django.db.models import Max

class ImportHistoryManager(models.Model):

    def last_successfull_dt(source):
        max_dt = super(ImportHistoryManager, self).get_queryset().filter(data_source=source, success=True).aggregate(Max('file_dt'))
        return max_dt['file_dt__max']

    def record_import(self, source, date, was_successful):
        import_record = self.create(file_dt=date, data_source=source, success=was_successful)
        return import_record
