import uuid
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)    

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55) 
    profile_image = models.ImageField(upload_to="BrandImage")

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=55)
    description = models.TextField()
    price = models.FloatField()
    profile_image =  models.ImageField(upload_to="ProductIDImage")
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="ProductImages")
