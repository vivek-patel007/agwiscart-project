from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
#from mycart.utils import unique_slug_generator
# Create your models here.

class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=128)
    description = models.CharField(max_length=300)
    slug=models.SlugField(unique=True,default="",null=True,blank=True)
    active=models.BooleanField(default=True)
    timestamp=models.DateTimeField()
    def __str__(self):
        return self.title

class subcategory(models.Model):
    subcategory_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=128)
    description = models.TextField(max_length=200)
    slug=models.SlugField(unique=True,default="",null=True,blank=True)
    thumbnail=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    timestamp=models.DateTimeField()
    def __str__(self):
        return self.title

class productimages(models.Model):
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    image = models.ImageField(upload_to="shop/images")
    featured=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    timestamp=models.DateTimeField()

    def __str__(self):
        return self.product.title
    

class product(models.Model):
    product_id  = models.AutoField(primary_key=True)
    brand_name  = models.CharField(max_length=128, null = True,blank=True)
    title       = models.CharField(max_length=50)
    category    = models.ForeignKey('category',related_name='Category',on_delete=models.CASCADE,default=1)
    subcategory = models.ForeignKey('subcategory',related_name='SubCategory',on_delete=models.CASCADE)
    price       = models.IntegerField()
    sell_price  = models.DecimalField(decimal_places=2,max_digits=100,default=10.99,null=True,blank=True)
    description = models.TextField()
    slug        = models.SlugField(unique=True,null=True,blank=True)
    pub_date    = models.DateField(auto_now_add=True,auto_now=False)
    active      = models.BooleanField(default=True)
    
    class Meta:
        unique_together = (('title','slug',),)
        constraints     = [
            models.UniqueConstraint(fields=['title', 'slug'], name='name of constraint')
        ]

    def get_price(self):
        return self.price

    def __str__(self):
        return self.title


def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=product)
