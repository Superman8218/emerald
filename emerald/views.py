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
        context['filter'] = self.filter
        return context
