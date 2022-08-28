from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from clients.serializers import ClientSerializer
from users.permissions import ClientPermission


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filterset_fields = ['company_name', 'email']
    search_fields = ['company_name', 'email']

    def get_queryset(self):
        employee = self.request.user.employee
        if employee.role == 'SALES':
            return Client.objects.filter(sales_contact=employee)
        elif employee.role == 'SUPPORT':
            return Client.objects.filter(
                contract__event__support_contact=employee
                ).distinct()
        elif employee.role == 'MANAGEMENT':
            return Client.objects.all()
        else:
            return Client.objects.none()

    def perform_create(self, serializer):
        employee = self.request.user.employee
        if employee.role == 'SALES':
            serializer.save(sales_contact=employee)
        serializer.save()
