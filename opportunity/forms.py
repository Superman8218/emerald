from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OpportunityFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(OpportunityFilterFormHelper, self).__init__(*args, **kwargs)
        self.form_id = 'id-OpportunityForm'
        self.form_class = 'form'
        self.form_method = 'get'

        self.add_input(Submit('submit', 'Submit'))
