from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address_street = models.CharField(max_length=100)
    address_city = models.CharField(max_length=50)
    address_state = models.CharField(max_length=50)
    address_postal_code = models.CharField(max_length=20)
    company_website = models.URLField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
