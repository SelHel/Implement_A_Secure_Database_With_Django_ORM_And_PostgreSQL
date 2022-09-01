from rest_framework.serializers import HyperlinkedModelSerializer

from users.serializers import EmployeeSerializer
from clients.models import Client


class ClientSerializer(HyperlinkedModelSerializer):
    sales_contact = EmployeeSerializer(read_only=True).fields['url']

    class Meta:
        model = Client
        fields = [
            'url',
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'mobile',
            'company_name',
            'sales_contact'
        ]
