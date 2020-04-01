from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'units', views.UnitViewSet, basename='units')
router.register(r'workforce', views.WorkforceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'api_rest'
urlpatterns = [
    path('', include(router.urls)),
    path('workforce/service/<int:service>/', views.WorkforceList.as_view(), name='workforce-service'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]