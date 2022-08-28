from django.shortcuts import get_object_or_404

from rest_framework.exceptions import NotAcceptable
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import get_event_serializer
from contracts.models import Contract
from users.permissions import EventPermission


class EventViewset(ModelViewSet):
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

    def get_serializer_class(self):
        return get_event_serializer(self.request.user.employee)

    def get_queryset(self):
        employee = self.request.user.employee
        if employee.role == 'SALES':
            return Event.objects.filter(contract__sales_contact=employee)
        elif employee.role == 'SUPPORT':
            return Event.objects.filter(support_contact=employee)
        elif employee.role == 'MANAGEMENT':
            return Event.objects.all()
        else:
            return Event.objects.none()

    def perform_create(self, serializer):
        employee = self.request.user.employee
        contracts = employee.contract.all()
        contract = get_object_or_404(
            Contract,
            pk=self.request.data.get('contract')
            )
        if contract not in list(contracts):
            raise NotAcceptable("You are not contract's sales contact.")
        if not contract.is_signed:
            raise NotAcceptable(
                "You cannot create an event for an unsigned contract"
                )

        serializer.save(contract=contract, client=contract.client)
