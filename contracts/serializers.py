from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        PrimaryKeyRelatedField)


from users.serializers import EmployeeSerializer
from contracts.models import Contract
from clients.models import Client


def get_contract_serializer(user):

    class ContractSerializer(HyperlinkedModelSerializer):
        sales_contact = EmployeeSerializer(read_only=True)
        client = PrimaryKeyRelatedField(
            queryset=Client.objects.filter(sales_contact=user)
            )

        class Meta:
            model = Contract
            fields = [
                'url',
                'id',
                'sales_contact',
                'client',
                'created_on',
                'updated_on',
                'is_signed',
                'amount',
                'payment_due'
            ]

        def to_representation(self, obj):
            ret = super().to_representation(obj)
            if user.role == 'SUPPORT':
                ret['amount'] = 'Non accessible'
            return ret

    return ContractSerializer
