from django.db import models
from shop.models import product
from django.contrib.auth.models import User
# Create your models here.

# class Cart(models.Model):
#     totle=models.DecimalField(default=10.99,max_digits=65,decimal_places=2)
#     active=models.BooleanField(default=True)
#     timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated=models.DateTimeField(auto_now_add=False,auto_now=True)

#     def __unicode__(self):
#         return "Cart ID is :%s"%(self.id)
#     def __str__(self):
#         return "Cart ID is :%s"%(self.id)
    
# class CartItem(models.Model):
#     cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True)
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     line_totle=models.DecimalField(default=10.99,max_digits=65,decimal_places=2)
#     timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated=models.DateTimeField(auto_now_add=False,auto_now=True)
#     def __str__(self):
#         try:
#             return str(self.cart.id)
#         except:
#             return self.product.title
    
#     def __unicode__(self):
#         try:
#             return str(self.cart.id)
#         except:
#             return self.product.title
class UserCart(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    payment_status=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self):
        return self.product.title
    def line_totle(self):
        return float(self.quantity * self.product.sell_price)
    
