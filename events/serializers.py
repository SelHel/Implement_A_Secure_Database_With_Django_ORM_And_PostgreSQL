from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from clients.serializers import ClientSerializer
from users.serializers import EmployeeSerializer
from events.models import Event
from contracts.models import Contract


def get_event_serializer(user):

    class EventSerializer(ModelSerializer):
        client = ClientSerializer(read_only=True)
        contract = PrimaryKeyRelatedField(
            queryset=Contract.objects.filter(
                sales_contact=user,
                is_signed=True)
            )
        support_contact = EmployeeSerializer(read_only=True)

        class Meta:
            model = Event
            fields = [
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
