from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsManagement

from users.serializers import UserSerializer


class EmployeeViewset(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsManagement]

    def get_queryset(self):
        return User.objects.all()
