# Django
import tempfile
from weasyprint import HTML
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

# Decorators
from django.contrib.auth.decorators import login_required

# Forms
from .forms import *

# Models
from .models import *

# Utilities
from decimal import Decimal
from .utils import render_to_pdf
from django.utils import timezone
import json


# Create your views here.

@login_required
def createDarasUser(request):
    """ Create Daras user view """
    form = CreateDarasUserForm()
    if request.method == 'POST':
        form = CreateDarasUserForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            username = data['username']
            password1 = data['password1']
            password2 = data['password2']

            member = User(username=username, password=password1)
            member.first_name = data['first_name']
            member.last_name = data['last_name']
            member.save()
            
            p = Profile()
            p.user = member
            p.is_client = False
            p.save()

            return redirect('budget:administration')

    return render(request, 'budget/create-user.html', {
        'form':form
    })

@login_required
def listDarasUsers(request):
    daras_users = Profile.objects.filter(is_client=False)
    return render(request, 'budget/list-users.html',{
        'daras_users':daras_users,
    })

@login_required
def createBudgetActivity(request):
    form = CreateActivityForm()
    services = Service.objects.filter(budget_type__slug='actividades')
    if request.method == 'POST':
        form = CreateActivityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            a = Activity()
            a.title = data['title']
            a.unit = data['unit']
            a.unit_value = data['unit_value']
            a.service = data['service']
            a.category = data['category']
            a.save()

            return redirect('budget:administration')

    return render(request, 'budget/create-activity.html', {
        'form':form,
        'services':services,
    })

@login_required
def listActivities(request):
    activities = Activity.objects.all()

    return render(request, 'budget/list-activities.html',{
        'activities':activities,
    })

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
def listClient(request):
    """ List clients """

    clients = Client.objects.all()
    return render(
        request=request,
        template_name='budget/list-clients.html', 
        context= 
        {
            'clients':clients,
        })

@login_required
def listBudgets(request):

    # Only render purposes
    form = CreateBudgetForm()

    budgets = Budget.objects.all().order_by('-created')
    return render(
        request=request,
        template_name='budget/list-budgets.html',
        context={
            'budgets': budgets,
            'form': form
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
            
            b.typeOf = data['typeOf']
            b.client = data['client']
            b.service = data['service']
            b.risk = data['risk']
            b.time = data['time']
            b.iva_option = data['iva_option']
            b.iva = data['iva']
            b.created_by = request.user.profile
            b.save()
            pk = b.id
            return redirect('budget:fill-budget', pk=pk)

@login_required
def fillBudget(request, pk):
    """ Fill Budget """
    budget = Budget.objects.get(id=pk)
    items = BudgetItem.objects.filter(budget=budget)
    clients = Client.objects.all()
    units = Unit.objects.all()
    form = FillBudgetForm()
    activities = Activity.objects.filter(service=budget.service)
    if request.method == "POST":
        form = FillBudgetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            b = budget
            b.consecutive = data['consecutive']
            b.client = data['client']
            b.subject = data['subject']
            b.delivery_time = data['delivery_time']
            b.rev_number = data['rev_number']
            b.aiu_over = data['aiu_over']
            b.iva_option = data['iva_option']
            b.comment = data['comment']
            b.utility_percentage = data['utility_percentage']
            b.incidentals_percentaje = data['incidentals_percentaje']
            b.administration_percentage = data['administration_percentage']
            b.save()

            return redirect('budget:budget-detail', budget_pk=pk)

    return render(
        request=request,
        template_name='budget/fill-budget.html',
        context={
            'clients': clients,
            'units': units,
            'budget': budget,
            'items': items,
            'activities':activities,
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
            'subitems': subitems,
        }
    )

@login_required
def editBudgetSubItem(request, budget_pk, item_pk, subitem_pk):
    """ Create APU for specific activity """

    budget = get_object_or_404(Budget, id=budget_pk)
    item = get_object_or_404(BudgetItem, id=item_pk)
    subitem = get_object_or_404(BudgetSubItem, id=subitem_pk)
    servicios = Service.objects.all()
    wfJson = []
    matJson = []
    equipJson = []
    
    if budget.service.slug == 'integral':
        # Building Workforce optgroups for select element (HTML)
        for i in range(len(servicios)):
            q = Workforce.objects.filter(service=servicios[i]).exists()
            if q:
                w = Workforce.objects.filter(service=servicios[i])
            else:
                # Avoid add 'Integral' label in json and select element (HTML)
                break

            aux = {
                "{}".format(servicios[i].name):list()
            }
            wfJson.append(aux)
            for j in w:
                aux2 = {
                    'id':'{}'.format(j.id),
                    'name':'{}'.format(j.name)
                }
                aux[servicios[i].name].append(aux2)
        wfJson = json.dumps(wfJson,ensure_ascii=False)
        # Building Material optgroups for select element (HTML)
        for i in range(len(servicios)):
            q = Material.objects.filter(service=servicios[i]).exists()
            if q:
                m = Material.objects.filter(service=servicios[i])
            else:
                # Avoid add 'Integral' label in json and select element (HTML)
                break
            aux = {
                '{}'.format(servicios[i].name):list()
            }
            matJson.append(aux)
            for j in m:
                aux2 = {
                    'id':'{}'.format(j.id),
                    'name':'{}'.format(j.name.replace('"', '\\"'))
                }
                aux[servicios[i].name].append(aux2)
        matJson = json.dumps(matJson,ensure_ascii=False)
        # Building Equipment and Tools optgroups for select element (HTML)
        for i in range(len(servicios)):
            q = Equipment.objects.filter(service=servicios[i]).exists()
            if q:
                e = Equipment.objects.filter(service=servicios[i])
            else:
                # Avoid add 'Integral' label in json and select element (HTML)
                break
            aux = {
                '{}'.format(servicios[i].name):list()
            }
            equipJson.append(aux)
            for j in e:
                aux2 = {
                    'id':'{}'.format(j.id),
                    'name':'{}'.format(j.name.replace('"', '\\"'))
                }
                aux[servicios[i].name].append(aux2)
        equipJson = json.dumps(equipJson,ensure_ascii=False)
        
    if request.method == 'POST':
        # Store 'value' of each row to calc the subitem unit value
        workforce = request.POST.getlist('workforce')
        wfamount = request.POST.getlist('wfamount')
        wfprice = request.POST.getlist('wfprice')
        wfperformance = request.POST.getlist('wfperformance')
        wfvalue = request.POST.getlist('wfvalue')

        WorkforceAPU.objects.filter(subitem=subitem).delete()
        for i, j, k, l, m in zip(workforce, wfamount, wfprice, wfperformance, wfvalue):
            w = WorkforceAPU()
            w.subitem = subitem
            aux = Workforce.objects.get(id=i)
            w.workforce = aux
            w.amount = j
            w.daily_price = k
            w.performance = Decimal(l)
            w.value = m
            w.save()

        material = request.POST.getlist('material')
        mamount = request.POST.getlist('mamount')
        mprice = request.POST.getlist('mprice')
        munit = request.POST.getlist('munit')
        mvalue = request.POST.getlist('mvalue')

        MaterialAPU.objects.filter(subitem=subitem).delete()
        for i, j, k, l, m in zip(material, mamount, mprice, munit, mvalue):
            mat = MaterialAPU()
            mat.subitem = subitem
            aux = Material.objects.get(id=i)
            mat.material = aux
            mat.amount = j
            mat.daily_price = k
            mat.unit = l
            mat.value = m
            mat.save()

        equipment = request.POST.getlist('equipment')
        equipamount = request.POST.getlist('equipamount')
        equipprice = request.POST.getlist('equipprice')
        equipperformance = request.POST.getlist('equipperformance')
        equipvalue = request.POST.getlist('equipvalue')

        EquipmentAPU.objects.filter(subitem=subitem).delete()
        for i, j, k, l, m in zip(equipment, equipamount, equipprice, equipperformance, equipvalue):
            e = EquipmentAPU()
            e.subitem = subitem
            aux = Equipment.objects.get(id=i)
            e.equipment = aux
            e.amount = j
            e.daily_price = k
            e.performance = Decimal(l)
            e.value = m
            e.save()

        transport = request.POST.getlist('transport')
        transpamount = request.POST.getlist('transpamount')
        transpprice = request.POST.getlist('transpprice')
        transpperformance = request.POST.getlist('transpperformance')
        transpvalue = request.POST.getlist('transpvalue')

        TransportAPU.objects.filter(subitem=subitem).delete()
        for i, j, k, l, m in zip(transport, transpamount, transpprice, transpperformance, transpvalue):
            t = TransportAPU()
            t.subitem = subitem
            aux = Transport.objects.get(id=i)
            t.transport = aux
            t.amount = j
            t.daily_price = k
            t.performance = Decimal(l)
            t.value = m
            t.save()

        secure = request.POST.getlist('secure')
        secureamount = request.POST.getlist('secureamount')
        secureprice = request.POST.getlist('secureprice')
        secureperformance = request.POST.getlist('secureperformance')
        securevalue = request.POST.getlist('securevalue')

        SecureAPU.objects.filter(subitem=subitem).delete()
        for i, j, k, l, m in zip(secure, secureamount, secureprice, secureperformance, securevalue):
            s = SecureAPU()
            s.subitem = subitem
            aux = Secure.objects.get(id=i)
            s.secure = aux
            s.amount = j
            s.daily_price = k
            s.performance = Decimal(l)
            s.value = m
            s.save()

        subtotal = request.POST.getlist('subtotal')
        aux = []
        # Avoid error at save Subtotals of APU (1 of 4) incomplete
        for i in subtotal:
            if i == '':
                aux.append(Decimal(0))
            else:
                aux.append(Decimal(i))

        subitem.unit_value = sum(aux)
        subitem.total_value = subitem.unit_value * subitem.amount
        subitem.apu_exists = True
        subitem.save()
        
        SubtotalAPU.objects.filter(budget=budget, subitem=subitem).delete()
        sub = SubtotalAPU(subitem=subitem)
        sub.budget = budget
        sub.workforce = aux[0]
        sub.material = aux[1]
        sub.equipment = aux[2]
        sub.transport = aux[3]
        sub.secure = aux[4]
        sub.total = sum(aux)
        sub.save()
        

        return redirect('budget:budget-detail', budget_pk=budget.id)

    return render(
        request=request,
        template_name='budget/create-apu.html',
        context={
            'budget': budget,
            'item': item,
            'subitem': subitem,
            'wfJson':wfJson,
            'matJson':matJson,
            'equipJson':equipJson
        }
    )

@login_required
def updateBudgetSubitem(request, budget_pk,item_pk, subitem_pk):
    """ Update subitem duration """
    budget = Budget.objects.get(id=budget_pk)
    subitem = BudgetSubItem.objects.get(id=subitem_pk, budget=budget)

    if request.method == 'POST':
        duration = request.POST.get('duration')
        rev_number = request.POST.get('rev_number')
        # import pdb; pdb.set_trace()
        s = subitem
        s.duration = duration
        s.rev_number = rev_number
        s.save()
        return redirect('budget:edit-subitem', budget_pk=budget_pk, item_pk=item_pk, subitem_pk=subitem_pk  )

@login_required
def PreviewAPU(request, budget_pk, item_pk, subitem_pk):
    budget = Budget.objects.get(id=budget_pk)
    item = BudgetItem.objects.get(id=item_pk)
    subitem = BudgetSubItem.objects.get(id=subitem_pk)

    workforce = WorkforceAPU.objects.filter(subitem=subitem)
    material = MaterialAPU.objects.filter(subitem=subitem)
    equipment = EquipmentAPU.objects.filter(subitem=subitem)
    transport = TransportAPU.objects.filter(subitem=subitem)
    secure = SecureAPU.objects.filter(subitem=subitem)

    subtotal = SubtotalAPU.objects.get(subitem=subitem)

    if budget.aiu_over == '2':
        admon_value =  round(Decimal(budget.administration_percentage/100) * subtotal.total,2)
        incident_value =  round(Decimal(budget.incidentals_percentaje/100) * subtotal.total,2)
        utility_value =  round(Decimal(budget.utility_percentage/100) * subtotal.total,2)
    else:
        admon_value = 0
        incident_value = 0
        utility_value = 0
    
    total = subtotal.total + admon_value + incident_value + utility_value
    data = {
        'budget': budget,
        'item': item,
        'subitem': subitem,
        'workforce': workforce,
        'material': material,
        'equipment': equipment,
        'transport': transport,
        'secure': secure,
        'subtotal':subtotal,
        'admon_value':admon_value,
        'incident_value':incident_value,
        'utility_value':utility_value,
        'total':total
    }

    pdf = render_to_pdf('budget/apu-preview.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
def PreviewBudget(request, budget_pk):
    budget = Budget.objects.get(id=budget_pk)
    items = BudgetItem.objects.filter(budget=budget)
    total_direct_cost = 0

    for i in range(len(items)):
        for j in range(len(items[i].subitems.all())):
            try:
                total_direct_cost += items[i].subitems.all()[j].total_value
            except:
                total_direct_cost = 0
    
    if budget.aiu_over == '1':
        administration_value = Decimal(budget.administration_percentage/100) * total_direct_cost
        incidentals_value = Decimal(budget.incidentals_percentaje/100) * total_direct_cost
        utility_value = Decimal(budget.utility_percentage/100) * total_direct_cost
    else:
        administration_value = 0
        incidentals_value = 0
        utility_value = 0

    total_indirect_cost = administration_value+incidentals_value+utility_value
    subtotal = total_direct_cost + total_indirect_cost
    if budget.iva_option == '1':
        iva_over = (budget.iva/100) * subtotal
    else:
        iva_over = (budget.iva/100) * utility_value
    total_cost = subtotal + iva_over

    data = {
        'budget': budget,
        'items': items,
        'total_direct_cost': total_direct_cost,
        'total_indirect_cost':total_indirect_cost,
        'administration_value': administration_value,
        'incidentals_value': incidentals_value,
        'utility_value': utility_value,
        'subtotal':subtotal,
        'iva_over':iva_over,
        'total_cost':total_cost,
    }

    pdf = render_to_pdf('budget/budget-preview.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

@login_required
def PanelAdmin(request):
    return render(request, 'budget/administration.html')