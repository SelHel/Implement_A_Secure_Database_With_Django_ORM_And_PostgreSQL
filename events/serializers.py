from rest_framework.serializers import (HyperlinkedModelSerializer,
                                        PrimaryKeyRelatedField)

from clients.serializers import ClientSerializer
from events.models import Event
from contracts.models import Contract


def get_event_serializer(user):

    class EventSerializer(HyperlinkedModelSerializer):
        client = ClientSerializer(read_only=True)
        contract = PrimaryKeyRelatedField(
            queryset=Contract.objects.filter(
                sales_contact=user,
                is_signed=True)
            )
        client = PrimaryKeyRelatedField(
            queryset=Contract.objects.filter(
                sales_contact=user)
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

    return EventSerializer
