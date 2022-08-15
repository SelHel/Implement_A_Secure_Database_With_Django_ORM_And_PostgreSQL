from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contracts.models import Contract
from contracts.serializers import ContractSerializer
from users.permissions import ContractPermision


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
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

    def get_queryset(self):
        return Contract.objects.all()


class MyContractsViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermision]

    def get_queryset(self):
        employee = self.request.user.employee
        if employee.role == 'SALES':
            return Contract.objects.filter(sales_contact=employee)
        else:
            return []
