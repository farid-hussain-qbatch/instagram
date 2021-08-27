# from typing import Generic
from typing import Generic
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.
class SuperMart(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    no_of_floors = models.IntegerField()
    class Meta:
        indexes=[
            models.Index(fields=['name',]),
        ]

    def __str__(self):
        return self.name
    

class Image(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')  
    name = models.CharField(max_length=100)
    url =  models.URLField()
    def __str__(self):
        return self.name
    @property
    def source(self):
        return self.content_object

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.BigIntegerField(null=False, blank=False, unique=True)
    address = models.TextField()
    super_marts = models.ForeignKey(SuperMart, on_delete=models.CASCADE)
    image = GenericRelation(Image, related_query_name='customer' )

    def __str__(self):
        return self.name


    
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    super_marts = models.ForeignKey(SuperMart, on_delete=models.CASCADE, null= True)
    customers = models.ManyToManyField(Customer, through='Order')
    image = GenericRelation(Image, related_query_name='product' )
    def __str__(self):
        return self.title
    
class Order(models.Model):
    date_of_order = models.DateField()
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Category(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Productversion(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    
    
    
    

    
    
    
    
    
    
