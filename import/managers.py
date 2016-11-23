from django.db import models

class ImportHistoryManager(models.Model):

    def last_successfull_dt():
        return_dt = super(ImportHistoryManager, self).get_queryset().filter(success=True).aggregate(Max('file_dt'))

    def record_import(self, date, was_successful):
        import_record = self.create(file_dt=date, success=was_successful)
        return import_record
