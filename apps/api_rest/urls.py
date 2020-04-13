from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'units', views.UnitViewSet, basename='units')
router.register(r'materials', views.MaterialViewSet, basename='materials')
router.register(r'transports', views.TransportViewSet, basename='transports')
router.register(r'secures', views.SecureViewSet, basename='secures')
router.register(r'workforce', views.WorkforceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api_rest'
urlpatterns = [
    path('', include(router.urls)),
    path('workforce/service/<int:service>/', views.WorkforceList.as_view(), name='workforce-service'),
    path('material/service/<int:service>/', views.MaterialList.as_view(), name='material-service'),
    path('equipment/service/<int:service>/', views.EquipmentList.as_view(), name='equipment-service'),
    path('budget/<int:budget_id>/create-item/', views.CreateBudgetItem.as_view(), name='create-item'),
    path('budget/<int:budget_pk>/add-subitem/<int:budgetItem_id>', views.addBudgetSubitem, name='add-subitem'),
    path('budget/<int:budget_slug>/item/<int:item_slug>/subitems', views.BudgetSubItemList.as_view(), name='budget-subitems'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]