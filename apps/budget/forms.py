# Forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Models
from .models import *
from django.contrib.auth.models import User


class CreateDarasUserForm(UserCreationForm, forms.ModelForm):
    username = forms.EmailField(max_length=50, required=True)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
        
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2')


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('nit', 'name', 'country', 'state', 'city', 'address')

class CreateBudgetForm(forms.ModelForm):
    """ Create Budget form """

    class Meta:
        model = Budget
        fields = (
            'typeOf',
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
            'delivery_time',
            'rev_number',
            'aiu_over',
            'comment',
            'utility_percentage',
            'incidentals_percentaje',
            'administration_percentage',
            'iva_option',
        )

class BudgetSubItemForm(forms.ModelForm):
    """ Budget items form"""

    def __init__(self, *args, **kwargs):
        super(BudgetSubItemForm, self).__init__(*args, **kwargs)
        self.fields['unit'].empty_label = "Unidades"

    class Meta:
        model = BudgetSubItem
        fields = ('description', 'unit', 'amount')

