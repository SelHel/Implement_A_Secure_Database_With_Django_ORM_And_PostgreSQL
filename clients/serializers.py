from rest_framework.serializers import ModelSerializer

from users.serializers import EmployeeSerializer
from clients.models import Client


class ClientSerializer(ModelSerializer):
    sales_contact = EmployeeSerializer(read_only=True)

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'sales_contact'
        ]
