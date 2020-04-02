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
x = Service.objects.get(id=1)
Equipment.objects.bulk_create([
Equipment(name="HTAS MENORES" , service=x, daily_price=100000),
Equipment(name="MAQUINA SOLDAR" , service=x, daily_price=35000),
Equipment(name="PULIDORAS" , service=x, daily_price=22500),
Equipment(name="ANDAMIOS 2X2X6 MTS" , service=x, daily_price=65000),
Equipment(name="ANDAMIOS 2X2X12 MTS" , service=x, daily_price=140000),
Equipment(name="MOTOSOLDADOR" , service=x, daily_price=180000),
Equipment(name="EXTENSIONES" , service=x, daily_price=22500),
Equipment(name="CONTENEDOR" , service=x, daily_price=35000),
Equipment(name="TILFORD" , service=x, daily_price=28500),
Equipment(name="EQUIPO DE OXICORTE" , service=x, daily_price=45000),
Equipment(name="MOTORTOOL" , service=x, daily_price=14500),
Equipment(name="CAMA BAJA" , service=x, daily_price=750000),
Equipment(name="MONTACARGA 7,5 TON" , service=x, daily_price=1450000),
Equipment(name="GRÚA 15 TON" , service=x, daily_price=1650000),
Equipment(name="GRÚA 30 TON" , service=x, daily_price=2250000),
Equipment(name="GRÚA 45 TON" , service=x, daily_price=3580000),
Equipment(name="GRÚA 120 TON" , service=x, daily_price=5500000),
Equipment(name="CAMIÓN GRÚA" , service=x, daily_price=1850000),
Equipment(name="CARPA" , service=x, daily_price=18500),
Equipment(name="CONTENEDOR DE ALMACEN 20 ft" , service=x, daily_price=28500),
Equipment(name="CONTENEDOR TIPO OFICINA 40 PIES" , service=x, daily_price=35000),
Equipment(name="BAÑO PORTATIL" , service=x, daily_price=14500),
Equipment(name="PLANTA ELECTRICA 30KVA" , service=x, daily_price=180000),
Equipment(name="PLANTA ELECTRICA 4KVA" , service=x, daily_price=85000),
Equipment(name="COMPRESOR DE AIRE" , service=x, daily_price=28500),
Equipment(name="EQUIPO AIRLESS" , service=x, daily_price=155000),
Equipment(name="TALADRO" , service=x, daily_price=12500),
])