from django.db import models

from users.models import User

class Client(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  email = models.EmailField(max_length=100, unique=True)
  phone = models.CharField(max_length=20, unique=True)
  mobile = models.CharField(max_length=20, unique=True)
  company_name = models.CharField(max_length=250)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  sales_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f"{self.company_name}"

