from django.db import models

from users.models import User
from clients.models import Client
from contracts.models import Contract


class Event(models.Model):
    name = models.CharField(max_length=150)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=User,on_delete=models.SET_NULL, null=True)
    is_finished = models.BooleanField(default=False)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"