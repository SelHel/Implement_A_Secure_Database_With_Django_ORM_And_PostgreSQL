from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


from users.serializers import EmployeeSerializer
from contracts.models import Contract
from clients.models import Client


def get_contract_serializer(user):

    class ContractSerializer(ModelSerializer):
        sales_contact = EmployeeSerializer(read_only=True)
        client = PrimaryKeyRelatedField(queryset=Client.objects.filter(sales_contact=user))

        class Meta:
            model = Contract
            fields = [
                'id',
                'sales_contact',
                'client',
                'created_on',
                'updated_on',
                'is_signed',
                'amount',
                'payment_due'
            ]

    return ContractSerializer
