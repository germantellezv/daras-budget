from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import *

# Models
from .models import *

# Create your views here.
@login_required
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
    """ Create budget with general/basic information """

    form = CreateBudgetForm()
    # form2 is imported only for render purposes ('units' select) in frontend
    form2= BudgetItemForm()
    
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

            titles = request.POST.getlist('title')
            units = request.POST.getlist('unit')
            amounts = request.POST.getlist('amount')

            if titles and units and amounts:
                for i,j,k in zip(titles,units,amounts):
                    I = BudgetItem()
                    I.budget = B
                    I.title = i
                    I.unit = Unit.objects.get(id=j)
                    I.amount = k
                    I.save()
                    aux = '{}{}'.format(B.client.nit, I.id)
                    I.slug=slugify(aux)
                    I.save()
            
            slug = B.slug
            return redirect('budget:budget-detail', slug=slug)

    return render(
        request=request, 
        template_name='budget/create-budget.html',
        context={
            'form':form,
            'form2':form2,
        })

@login_required
def budgetDetail(request, slug):
    """ Budget summary before edit items """
    budget = Budget.objects.get(slug=slug)
    items = BudgetItem.objects.filter(budget=budget)
    return render(
        request=request,
        template_name='budget/budget-detail.html',
        context={
            'budget':budget,
            'items':items,
        }
        )

@login_required
def editBudgetItem(request, slug, code):
    """ Edit budget item """
    budget = get_object_or_404(Budget, slug=slug)
    item = get_object_or_404(BudgetItem, slug=code)

    return render(
        request=request,
        template_name = 'budget/edit-item.html',
        context={
            'item':item,
            'budget':budget,
        }
    )
