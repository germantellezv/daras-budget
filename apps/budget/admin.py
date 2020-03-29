from django.contrib import admin

# Models
from .models import *

# Register your models here.

@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Clientes"

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    class Meta:
        verbose_name = "Tipos de servicio"

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Presupuesto"