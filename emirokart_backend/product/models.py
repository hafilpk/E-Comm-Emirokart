from django.db import models


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='media/category/', blank=True, null=True)
    description=models.TextField()
    display_order=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/')
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name