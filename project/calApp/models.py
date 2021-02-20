from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name
