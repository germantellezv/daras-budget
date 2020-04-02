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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]