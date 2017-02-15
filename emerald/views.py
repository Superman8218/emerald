from collections import OrderedDict

from django.shortcuts import render

from django_tables2 import SingleTableView

import pdb

def index(request):
    return render(request, 'emerald/index.html')

def landing(request):
    return render(request, 'emerald/landing-page-email-list.html')

# Generic filtered table view

class FilteredSingleTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        self.filter = self.filter_class(self.request.GET, queryset=super(FilteredSingleTableView, self).get_table_data())
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)

        self.filter.form.helper = self.helper_class()

        table = context['table']

        # Make the filter form fields match the contents and order of the table columns

        column_headers = [column.name for column in table.columns]
        new_fields = OrderedDict()

        for column_name in column_headers:
            if column_name in self.filter.form.fields:
                new_fields[column_name] = self.filter.form.fields[column_name]

        self.filter.form.fields = new_fields
        context['filter'] = self.filter

        # Add an offset to tell the table how many columns the filter should be offset by

        if hasattr(table, 'offset'):
            context['offset_range'] = range(table.offset)
        # pdb.set_trace()

        return context
