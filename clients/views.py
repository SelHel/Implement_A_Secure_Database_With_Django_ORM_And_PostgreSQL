from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()
