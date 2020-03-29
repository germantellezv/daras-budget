from django import forms

# Models
from .models import *

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('nit','name','country','state','city','address')

class CreateBudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('client','service','subject','administration_percentage','incidentals_percentaje','utility_percentage','iva_option','comment')
    def __init__(self, *args, **kwargs):
        super(CreateBudgetForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = "Selecciona un cliente"
        self.fields['service'].empty_label = "Selecciona un tipo de servicio"