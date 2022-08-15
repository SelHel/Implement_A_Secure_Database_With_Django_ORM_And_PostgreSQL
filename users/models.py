from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):

    MANAGEMENT = 'MANAGEMENT'
    SUPPORT = 'SUPPORT'
    SALES = 'SALES'

    ROLE_CHOICES = [
        (MANAGEMENT, 'management'),
        (SUPPORT, 'support'),
        (SALES, 'sales')
        ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='employee'
        )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
