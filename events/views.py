from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Event
from events.serializers import EventSerializer


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.all()
