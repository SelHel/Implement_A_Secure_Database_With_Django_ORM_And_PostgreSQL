from django.shortcuts import get_object_or_404

from rest_framework.exceptions import NotAcceptable
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contracts.models import Contract
from clients.models import Client
from contracts.serializers import get_contract_serializer
from users.permissions import ContractPermision


class ContractViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, ContractPermision]
    filterset_fields = [
        'created_on',
        'amount',
        'client__email',
        'client__company_name',
        'client__id'
        ]
    search_fields = [
        'created_on',
        'amount',
        'client__email',
        'client__company_name',
        'client__id'
        ]

    def get_serializer_class(self):
        return get_contract_serializer(self.request.user.employee)

    def get_queryset(self):
        employee = self.request.user.employee
        if employee.role == 'SALES':
            return Contract.objects.filter(sales_contact=employee)
        elif employee.role == 'SUPPORT':
            return Contract.objects.filter(event__support_contact=employee)
        elif employee.role == 'MANAGEMENT':
            return Contract.objects.all()
        else:
            return Contract.objects.none()

    def perform_create(self, serializer):
        employee = self.request.user.employee
        clients = employee.client.all()
        client = get_object_or_404(Client, pk=self.request.data.get('client'))
        if client not in list(clients):
            raise NotAcceptable("You are not client's sales contact")
        if employee.role == 'SALES':
            serializer.save(client=client, sales_contact=employee)
        serializer.save(client=client)
