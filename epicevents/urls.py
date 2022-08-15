from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from clients.views import ClientViewset, MyClientsViewset
from contracts.views import ContractViewset, MyContractsViewset
from events.views import EventViewset, MyEventsViewset
from users.views import UserViewset

router = routers.SimpleRouter()
router.register('clients', ClientViewset, basename='clients')
router.register('my-clients', MyClientsViewset, basename='my-clients')
router.register('contracts', ContractViewset, basename='contracts')
router.register('my-contracts', MyContractsViewset, basename='my-contracts')
router.register('events', EventViewset, basename='events')
router.register('my-events', MyEventsViewset, basename='my-events')
router.register('users', UserViewset, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
]
