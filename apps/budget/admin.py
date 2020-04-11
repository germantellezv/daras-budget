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
    list_display = ('description','slug','created','modified')
    class Meta:
        verbose_name = "Item de presupuesto"

@admin.register(BudgetSubItem)
class BudgetSubItemAdmin(admin.ModelAdmin):
    list_display = ('description','unit','slug')
    class Meta:
        verbose_name = "Subitem de presupuesto"



@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name','unit','service','daily_price','created','modified')
    # list_editable = ('unit','daily_price')
    readonly_fields = ('slug',)
    class Meta:
        verbose_name = "Materiales"

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name','service','daily_price','created','modified')
    # list_editable = ('unit','daily_price')
    readonly_fields = ('slug',)
    class Meta:
        verbose_name = "Equipos y herramientas"

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('name','daily_price','created','modified')
    # list_editable = ('unit','daily_price')
    readonly_fields = ('slug',)
    class Meta:
        verbose_name = "Transportes"
