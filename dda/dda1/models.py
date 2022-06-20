from django.db import models


# Create your models here.


class Persons(models.Model):
    name = models.CharField(max_length=100)
    pasn = models.CharField(max_length=100, default=0000)