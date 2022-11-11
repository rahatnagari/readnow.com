from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=11)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
