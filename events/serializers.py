from rest_framework.serializers import ModelSerializer

from events.models import Event


class EventSerializer(ModelSerializer):

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
