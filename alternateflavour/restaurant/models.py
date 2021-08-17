from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.number
