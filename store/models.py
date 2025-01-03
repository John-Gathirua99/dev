from django.db import models
import datetime
from django.contrib import messages
# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    
    first_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    email=models.EmailField()
    password= models.CharField(max_length=16)
    def __str__(self):
        return f'{self.first_name} {self.second_name}'



class Product(models.Model):
    name=models.CharField(max_length=60)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.TextField()
    image=models.ImageField(default='default.jpg',upload_to='uploads/products/')

    is_sale = models.BooleanField(default=False)

    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)

    def __str__(self):
        return self.name


class Orders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address=models.CharField(max_length=100,default='',blank=True)
    phone=models.CharField(max_length=10,blank=True,default='')
    date=models.DateTimeField(default=datetime.datetime.today)
    status= models.BooleanField(default=False)

    def __str__(self):
        return self.product

    
