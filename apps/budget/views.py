from django.shortcuts import get_object_or_404, render, redirect

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
    return render(
        request=request,
        template_name='budget/index.html'
        )

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
            'form': form
        })

@login_required
def listBudgets(request):

    # render form
    form = CreateBudgetForm()

    budgets = Budget.objects.all().order_by('-created')
    return render(
        request=request,
        template_name='budget/list-budgets.html',
        context={
            'budgets':budgets,
            'form':form
        }
        )

@login_required
def createBudget(request):
    """ Basic creation of budget """

    if request.method == 'POST':
        form = CreateBudgetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            b = Budget()
            b.client = data['client']
            b.save()
            
            pk = b.id
            return redirect('budget:fill-budget', pk=pk)
    request

@login_required
def fillBudget(request, pk):
    """ Fill Budget """

    budget = Budget.objects.get(id=pk)
    items = BudgetItem.objects.filter(budget=budget)
    clients = Client.objects.all()
    units = Unit.objects.all()
    form = EditBudgetForm()
    return render(
        request=request,
        template_name='budget/fill-budget.html',
        context={
            'clients':clients,
            'units':units,
            'budget':budget,
            'items':items,
            'form': form,
        }
    )

@login_required
def budgetDetail(request, budget_pk):
    """ Budget summary before edit items """

    budget = Budget.objects.get(id=budget_pk)
    items = BudgetItem.objects.filter(budget=budget)
    return render(
        request=request,
        template_name='budget/budget-detail.html',
        context={
            'budget': budget,
            'items': items,
        }
    )

@login_required
def editBudgetItem(request, slug, slug_item):
    """ Add specific activites to each activity """

    budget = get_object_or_404(Budget, slug=slug)
    item = get_object_or_404(BudgetItem, slug=slug_item)
    subitems = BudgetSubItem.objects.filter(budget=budget, item=item)

    if request.method == 'POST':

        descriptions = request.POST.getlist('description')
        units = request.POST.getlist('unit')
        amounts = request.POST.getlist('amount')
        unit_value = request.POST.getlist('value')

        if descriptions and units and amounts:
            for d, u, a, v in zip(descriptions, units, amounts, unit_value):
                S = BudgetSubItem()
                S.budget = budget
                S.item = item
                S.description = d
                aux = get_object_or_404(Unit, id=u)
                S.unit = aux
                S.amount = a
                # S.unit_value = v
                S.save()
            return redirect('budget:budget-detail', slug=slug)

    return render(
        request=request,
        template_name='budget/edit-item.html',
        context={
            'budget': budget,
            'item': item,
            'subitems':subitems,
        }
    )

@login_required
def editBudgetSubItem(request, slug, slug_item, slug_subitem):
    """ Create APU for specific activity """
    budget = get_object_or_404(Budget, slug=slug)
    item = get_object_or_404(BudgetItem, slug=slug_item)
    subitem = get_object_or_404(BudgetSubItem, slug=slug_subitem, budget=budget, item=item)
    return render(
        request=request,
        template_name='budget/edit-subitem.html',
        context={
            'item': item,
            'budget': budget,
            'subitem': subitem,
        }
    )
