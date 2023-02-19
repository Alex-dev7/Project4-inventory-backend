from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    department = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    details = models.CharField(max_length=250)
    location = models.CharField(max_length=20)