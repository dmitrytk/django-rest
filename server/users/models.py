from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)