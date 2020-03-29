from django.shortcuts import render, redirect


# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import CreateClientForm, CreateBudgetForm

# Models
from .models import Clients

# Create your views here.
def home(request):
    return render(request, 'budget/index.html')

@login_required
def budgetPanel(request):
    """ Choose type of service """
    return render(request, 'budget/choose.html')

@login_required
def createClient(request):
    form = CreateClientForm()
    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            c = Clients()
            c.nit = data['nit']
            c.name = data['name']
            c.country = data['country']
            c.state = data['state']
            c.city = data['city']
            c.address = data['address']
            c.save()
            return redirect('budget:choose')

    return render(
        request=request, 
        template_name='budget/create-client.html',
        context={
            'form':form
        })

@login_required
def createBudge(request):
    form = CreateBudgetForm()

    if request.method == 'POST':
        import pdb; pdb.set_trace()
        return redirect('home:login')

    return render(
        request=request, 
        template_name='budget/create-budget.html',
        context={
            'form':form,
        })




