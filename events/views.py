from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import EventSerializer
from users.permissions import EventPermission


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]
    filterset_fields = [
        'event_date',
        'client__company_name',
        'client__email',
        'client__id'
        ]
    search_fields = [
        'event_date',
        'client__company_name',
        'client__email',
        'client__id'
        ]

    def get_queryset(self):
        return Event.objects.all()


class MyEventsViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]

    def get_queryset(self):
        employee = self.request.user.employee
        if employee.role == 'SUPPORT':
            return Event.objects.filter(support_contact=employee)
        elif employee.role == 'SALES':
            return Event.objects.filter(contract__sales_contact=employee)
        else:
            return []
