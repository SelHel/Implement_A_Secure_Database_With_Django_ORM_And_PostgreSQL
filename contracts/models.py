from django.db import models

from users.models import Employee
from clients.models import Client


class Contract(models.Model):
    sales_contact = models.ForeignKey(
        to=Employee,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': Employee.SALES},
        related_name='contract'
        )
    client = models.ForeignKey(
        to=Client,
        on_delete=models.SET_NULL,
        null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_signed = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateField()

    def __str__(self):
        return f"{self.id} : {self.client.company_name} {self.created_on}"
