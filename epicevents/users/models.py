from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    MANAGEMENT = 'MANAGEMENT'
    SUPPORT = 'SUPPORT'
    SALES = 'SALES'
    
    ROLE_CHOICES = [
        (MANAGEMENT, 'management'),
        (SUPPORT, 'support'),
        (SALES, 'sales')
        ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)