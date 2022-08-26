from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from clients.views import ClientViewset
from contracts.views import ContractViewset
from events.views import EventViewset

router = routers.SimpleRouter()
router.register('clients', ClientViewset, basename='clients')
router.register('contracts', ContractViewset, basename='contracts')
router.register('events', EventViewset, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
]
