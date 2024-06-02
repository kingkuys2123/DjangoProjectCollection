from django.db import models

# Create your models here.
class WarehouseItem(models.Model):
    ItemName = models.CharField(max_length=100)
    Description = models.TextField()
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)