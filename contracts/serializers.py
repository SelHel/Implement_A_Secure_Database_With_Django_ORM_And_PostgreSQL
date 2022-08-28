from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        SerializerMethodField)


from users.serializers import EmployeeSerializer
from contracts.models import Contract
from clients.models import Client


def get_contract_serializer(user):

    class ContractSerializer(ModelSerializer):
        sales_contact = EmployeeSerializer(read_only=True)
        client = PrimaryKeyRelatedField(
            queryset=Client.objects.filter(sales_contact=user)
            )
        amount = SerializerMethodField('get_amount')

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

        def get_amount(self, contract):
            if user.role == 'SUPPORT':
                return "Non accessible"
            else:
                return contract.amount

    return ContractSerializer
