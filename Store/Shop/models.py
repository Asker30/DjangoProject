from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
