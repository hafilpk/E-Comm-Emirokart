from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=10,choices=(('Admin','Admin'),('User','User'),('Seller','Seller'),('Customer','Customer')))
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='user_shipping_address')
    address_type=models.CharField(max_length=50,choices=(('Home','Home'),('Office','Office')))
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)    