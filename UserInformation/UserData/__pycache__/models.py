from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=64)
    building=models.CharField(max_length=3)
    roomno=models.CharField(max_length=2)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, phone: {self.phone}"
