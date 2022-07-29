from django.db import models

from users.models import User
from clients.models import Client

class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_signed = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()
    
    def __str__(self):
        return f"{self.client.company_name} {self.created_on}"