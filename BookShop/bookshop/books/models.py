from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()