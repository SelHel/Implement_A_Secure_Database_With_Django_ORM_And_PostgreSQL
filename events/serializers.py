from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'client',
            'contract',
            'support_contact',
            'is_finished',
            'attendees',
            'event_date',
            'notes'
        )
