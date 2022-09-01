from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        PrimaryKeyRelatedField)

from clients.serializers import ClientSerializer
from events.models import Event
from contracts.models import Contract
from contracts.serializers import get_contract_serializer


def get_event_serializer(user, method):

    class EventSerializer(HyperlinkedModelSerializer):
        client = ClientSerializer(read_only=True).fields['url']
        contract = PrimaryKeyRelatedField(
            queryset=Contract.objects.filter(
                sales_contact=user,
                is_signed=True)
            )

        class Meta:
            model = Event
            fields = [
                'url',
                'id',
                'name',
                'client',
                'contract',
                'support_contact',
                'is_finished',
                'attendees',
                'event_date',
                'notes'
            ]

    class PutEventSerializer(HyperlinkedModelSerializer):
        client = ClientSerializer(read_only=True).fields['url']
        contract = get_contract_serializer(user)(read_only=True).fields['url']

        class Meta:
            model = Event
            fields = [
                'url',
                'id',
                'name',
                'client',
                'contract',
                'support_contact',
                'is_finished',
                'attendees',
                'event_date',
                'notes'
            ]

    if method == 'PUT':
        return PutEventSerializer

    return EventSerializer
