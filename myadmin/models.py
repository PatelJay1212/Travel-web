from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=250)

class Packages(models.Model):
    name = models.CharField(max_length=250) 
    destination = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    days = models.IntegerField()
    nights = models.IntegerField()
    person = models.IntegerField()
    description = models.CharField(max_length=750)
    image = models.ImageField(upload_to='package_pics')
