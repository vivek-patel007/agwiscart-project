from django.db import models
from cart.models import UserCart
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE,default=3)
    cart_ids=models.CharField(max_length=60,default=0)
    product_ids=models.CharField(max_length=60,default=0)
    invoice_id=models.CharField(max_length=60,default=0)
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
    amount=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)
    processed_on=models.DateTimeField(auto_now_add=True)



