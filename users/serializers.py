from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from users.models import Employee


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = ['role']


class UserSerializer(ModelSerializer):
    profile = EmployeeSerializer(source='employee')

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile'
        ]
