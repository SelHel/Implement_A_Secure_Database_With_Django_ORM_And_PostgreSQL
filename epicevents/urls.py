from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from clients.views import ClientViewset
from contracts.views import ContractViewset
from events.views import EventViewset
from users.views import EmployeeViewset

router = DefaultRouter()
router.register('clients', ClientViewset, basename='client')
router.register('contracts', ContractViewset, basename='contract')
router.register('events', EventViewset, basename='event')
router.register('employees', EmployeeViewset, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
]
