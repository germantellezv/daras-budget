from django import forms

# Models
from .models import *

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nit','name','country','state','city','address')

class CreateBudgetForm(forms.ModelForm):
    """ Create budget form """
    def __init__(self, *args, **kwargs):
        super(CreateBudgetForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = "Selecciona un cliente"
        self.fields['service'].empty_label = "Selecciona un tipo de servicio"
        self.fields['risk'].empty_label = "Selecciona un tipo de riesgo"
    
    class Meta:
        model = Budget
        fields = ('client',
        'risk',
        'time',
        'comment',
        'service',
        'subject',
        'iva_option',
        'utility_percentage',
        'incidentals_percentaje',
        'administration_percentage',
        )

class BudgetItemForm(forms.ModelForm):
    """ Budget items form"""
    def __init__(self, *args, **kwargs):
        super(BudgetItemForm, self).__init__(*args, **kwargs)
        self.fields['unit'].empty_label = "Unidades"
        
    class Meta:
        model = BudgetItem
        fields = ('title','unit','amount')