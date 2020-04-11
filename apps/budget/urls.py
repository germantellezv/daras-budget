
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
    path('panel/crear/cliente/', views.createClient, name='create-client'),
    path('panel/ver/presupuestos/', views.listBudgets, name='list-budgets' ),
    path('panel/crear/presupuesto/', views.createBudget, name='create-budget' ),
    path('panel/completar/presupuesto/<int:pk>', views.fillBudget, name='fill-budget'),
    path('panel/presupuesto/<slug:slug>/detalle', views.budgetDetail, name='budget-detail' ),
    path('panel/presupuesto/<slug:slug>/item/<slug:slug_item>/', views.editBudgetItem, name='edit-item' ),
    path('panel/presupuesto/<slug:slug>/item/<slug:slug_item>/subitem/<slug:slug_subitem>', views.editBudgetSubItem, name='edit-subitem'),
]