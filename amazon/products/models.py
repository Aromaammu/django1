from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=2000)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=4000)
