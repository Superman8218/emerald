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

        # Make the filter form columns match the table columns

        # pdb.set_trace()
        column_headers = [column.name for column in context['table'].columns]
        # for key in self.filter.form.fields:
            # print key
        # self.filter.form.fields = { key: self.filter.form[key] for key in self.filter.form.fields if key in column_headers }
        # filtered_fields = OrderedDict()
        for key in self.filter.form.fields:
            # if key in column.headers:
                # filtered_fields[key] = self.filter.form[key]
            if key not in column_headers:
                del self.filter.form.fields[key]
        # self.filter.form.fields = filtered_fields
        # pdb.set_trace()

        context['filter'] = self.filter

        return context
