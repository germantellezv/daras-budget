from django.shortcuts import render, redirect


# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import CreateClientForm, CreateBudgetForm

# Models
from .models import *

# Create your views here.
def panel(request):
    """ Panel view """
    return render(request, 'budget/index.html')

@login_required
def createClient(request):
    """ Client creation view """
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            c = Client()
            c.nit = data['nit']
            c.name = data['name']
            c.country = data['country']
            c.state = data['state']
            c.city = data['city']
            c.address = data['address']
            c.save()
            return redirect('budget:panel')

    return render(
        request=request, 
        template_name='budget/create-client.html',
        context={
            'form':form
        })

@login_required
def createBudge(request):
    """ Create budget with general information """
    form = CreateBudgetForm()

    if request.method == 'POST':
        form = CreateBudgetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            B = Budget()
            B.client = data['client']
            B.subject = data['subject']
            B.risk = data['risk']
            B.time = data['time']
            B.service = data['service']
            B.iva_option = data['iva_option']
            B.utility_percentage = data['utility_percentage']
            B.incidentals_percentaje = data['incidentals_percentaje']
            B.administration_percentage = data['administration_percentage']
            B.comment = data['comment']
            B.save()

            slug = B.slug

            return redirect('budget:complete-budget', slug=slug)

    return render(
        request=request, 
        template_name='budget/create-budget.html',
        context={
            'form':form,
        })

def completeBudge(request, slug):

    budget = Budget.objects.get(slug=slug)
    
    return render(
        request=request,
        template_name='budget/complete-budget.html',
        context={
            'budget':budget
        }
        )


