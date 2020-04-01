from django.contrib import admin

# Models
from .models import *

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Clientes"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    class Meta:
        verbose_name = "Tipos de servicio"

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('slug', 'client', 'service', 'subject')
    class Meta:
        verbose_name = "Presupuesto"

@admin.register(Workforce)
class WorkforceAdmin(admin.ModelAdmin):
    list_display = ('name','service','experience_time','daily_salary','created')
    list_editable = ('experience_time',)
    class Meta:
        verbose_name = "Mano de obra"

@admin.register(Risk)
class RiskAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Tipo de riesgo"

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Unidades"

@admin.register(BudgetItem)
class BudgetItemAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Item de presupuesto"