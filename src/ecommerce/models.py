from django.db import models

# Create your models here.
class ProductModel (models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(null=0.0)
    description = models.TextField(null='Sin descripción')
    seller = models.CharField(max_length=100, null='N/A')
    color = models.CharField(max_length=100, null='Sin color')
    dimensions = models.FloatField(null=0.0)