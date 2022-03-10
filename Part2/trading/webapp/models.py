from pyexpat import model
from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)

    def __str___(self):
        return self.user_name


class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    abv = models.CharField(default="$", max_length=5)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def getPrice(self):
        return self.price