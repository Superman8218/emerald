from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class FboMasterFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(FboMasterFilterFormHelper, self).__init__(*args, **kwargs)
        self.form_id = 'id-FboMasterForm'
        self.form_class = 'form'
        self.form_method = 'get'

        self.add_input(Submit('submit', 'Submit'))
