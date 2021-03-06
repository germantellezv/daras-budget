
"""daras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Views
from . import views

app_name = 'budget'
urlpatterns = [
    path('panel/', views.panel, name='panel' ),
    path('panel/crear/usuario/', views.createDarasUser, name='create-daras-user'),
    path('panel/editar/usuario/<int:user_id>', views.editDarasUser, name='edit-daras-user'),
    path('panel/crear/cliente/', views.createClient, name='create-client'),
    path('panel/crear/actividad/', views.createBudgetActivity, name='create-activity'),
    path('panel/ver/actividades/', views.listActivities, name='list-activities'),
    path('panel/ver/clientes/', views.listClient, name='list-client'),
    path('panel/ver/usuarios/', views.listDarasUsers, name='list-users'),
    path('panel/ver/presupuestos/', views.listBudgets, name='list-budgets' ),
    path('panel/crear/presupuesto/', views.createBudget, name='create-budget' ),
    path('panel/completar/presupuesto/<int:pk>', views.fillBudget, name='fill-budget'),
    path('panel/presupuesto/<int:budget_pk>/detalle', views.budgetDetail, name='budget-detail' ),
    path('panel/presupuesto/<slug:slug>/item/<slug:slug_item>/', views.editBudgetItem, name='edit-item' ),
    path('panel/presupuesto/<int:budget_pk>/item/<int:item_pk>/subitem/<int:subitem_pk>/apu/', views.editBudgetSubItem, name='edit-subitem'),
    path('panel/presupuesto/<int:budget_pk>/item/<int:item_pk>/actualizar/subitem/<int:subitem_pk>/', views.updateBudgetSubitem, name='update-subitem'),
    path('panel/preview/presupuesto/<int:budget_pk>/',views.PreviewBudget, name="preview-budget"),
    path('panel/preview/presupuesto/<int:budget_pk>/item/<int:item_pk>/subitem/<int:subitem_pk>/', views.PreviewAPU, name='preview-apu'),
    path('panel/admin/', views.PanelAdmin, name='administration' ),

]