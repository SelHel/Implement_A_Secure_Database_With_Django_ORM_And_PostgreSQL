from rest_framework import serializers

from contracts.models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = (
            'id',
            'sales_contact',
            'client',
            'is_signed',
            'amount',
            'payment_due'
        )
