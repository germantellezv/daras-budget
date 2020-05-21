from apps.budget.models import Workforce, Service
x = Service.objects.get(id=1)
Workforce.objects.bulk_create([
Workforce(service=x,name="SUP. MECÁNICO I",daily_salary=179096.31),
Workforce(service=x,name="SUP. MECÁNICO II",daily_salary=144699.62),
Workforce(service=x,name="SUP. MECÁNICO III",daily_salary=124699.62),
Workforce(service=x,name="SUP. MECÁNICO IV",daily_salary=85699.62),
Workforce(service=x,name="PROFESIONAL HSE",daily_salary=144699.62),
Workforce(service=x,name="VIGIA HSE",daily_salary=124699.62),
Workforce(service=x,name="SOLDADOR I",daily_salary=175620.00),
Workforce(service=x,name="SOLDADOR II",daily_salary=145620.00),
Workforce(service=x,name="SOLDADOR III",daily_salary=125620.00),
Workforce(service=x,name="SOLDADOR IV",daily_salary=115620.00),
Workforce(service=x,name="ARMADOR I",daily_salary=175620.00),
Workforce(service=x,name="ARMADOR II",daily_salary=145620.00),
Workforce(service=x,name="ARMADOR III",daily_salary=125620.00),
Workforce(service=x,name="ARMADOR IV",daily_salary=115620.00),
Workforce(service=x,name="AYUDANTE TEC.",daily_salary=113350.38),
Workforce(service=x,name="PINTOR",daily_salary=98335.38),
])


from apps.budget.models import Equipment, Service
x = Service.objects.get(id=2)
Equipment.objects.bulk_create([
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
Equipment(name="", service=x, daily_price=),
])


from apps.budget.models import Activity, ActivityCategory, Service
s=Service.objects.get(id=4)
c=ActivityCategory.objects.get(id=20)
Activity.objects.bulk_create([
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
    Activity(title='', unit_value=, category=c, service=s),
])