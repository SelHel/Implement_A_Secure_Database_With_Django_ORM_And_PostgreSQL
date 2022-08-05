from rest_framework.serializers import ModelSerializer

from contracts.models import Contract


class ContractSerializer(ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'sales_contact',
            'client',
            'is_signed',
            'amount',
            'payment_due'
        ]
