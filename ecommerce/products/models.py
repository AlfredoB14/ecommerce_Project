from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.TextField(default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTL5UMX3Vv8t5CzcGOIhMClknq7AOSttL7yj4RAkYCSAg&s")

    def __str__(self):
        return self.name #DEBE SER STRING
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name 