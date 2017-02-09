from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ContactFilterFormHelper, self).__init__(*args, **kwargs)
        self.form_id = 'id-ContactForm'
        self.form_class = 'form'
        self.form_method = 'get'

        self.add_input(Submit('submit', 'Submit'))
