from django.db import models
from cart.models import UserCart
from django.contrib.auth.models import User
# Create your models here.
# class cart_Items(models.Model):
#     products=models.ManyToManyField(UserCart)
class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    cart=models.ManyToManyField(UserCart,default=1)
    first_name=models.CharField(max_length=90)
    last_name=models.CharField(max_length=90)
    state=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    address2=models.CharField(max_length=111,null=True,blank=True)
    city=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")
    email=models.CharField(max_length=111)
    amount=models.DecimalField(decimal_places=2,max_digits=100,default=00.00,null=True,blank=True)
    