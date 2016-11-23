from django.db import models
from django.db.models import Max

class ImportHistoryManager(models.Model):

    def last_successfull_dt():
        max_dt = super(ImportHistoryManager, self).get_queryset().filter(success=True).aggregate(Max('file_dt'))
        return max_dt['file_dt__max']

    def record_import(self, date, was_successful):
        import_record = self.create(file_dt=date, success=was_successful)
        return import_record
