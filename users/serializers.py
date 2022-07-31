from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('role')


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(source='employee')

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name'
            'last_name',
            'email',
            'employee'
        )
