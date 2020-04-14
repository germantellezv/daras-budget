from django import forms

# Models
from .models import *


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nit', 'name', 'country', 'state', 'city', 'address')


class CreateBudgetForm(forms.ModelForm):
    """ Create Budget form """

    class Meta:
        model = Budget
        fields = (
            'client',
            'risk',
            'time',
            'service',
            'iva_option',
            'iva',
        )


class FillBudgetForm(forms.ModelForm):
    """ Fill budget form """

    class Meta:
        model = Budget
        fields = (
            'consecutive',
            'client',
            'subject',
            'comment',
            'utility_percentage',
            'incidentals_percentaje',
            'administration_percentage',
        )


class BudgetSubItemForm(forms.ModelForm):
    """ Budget items form"""

    def __init__(self, *args, **kwargs):
        super(BudgetSubItemForm, self).__init__(*args, **kwargs)
        self.fields['unit'].empty_label = "Unidades"

    class Meta:
        model = BudgetSubItem
        fields = ('description', 'unit', 'amount')

