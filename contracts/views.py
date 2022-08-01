from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contract.objects.all()
