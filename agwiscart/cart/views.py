from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from cart.models import UserCart
from shop.models import product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def carts(request):
    cart=UserCart.objects.filter(owner__id=request.user.id)
    totle_item=cart.count()
    contex={'item':cart,'totle':totle_item}
    return render(request, 'cart/cart.html',contex)
@login_required
def update_cart(request,slug, pid):
    try:
        prods=product.objects.get(slug=slug,product_id=pid)
        userr = User.objects.get(username=request.user)
        cart=UserCart.objects.get_or_create(owner=userr,product=prods,quantity=1)
        is_exist=UserCart.objects.filter(product=prods.product_id,owner=request.user.id)
        if len(is_exist)>1:
            messages.warning(request,"Item Already Exist In Your Cart")
        return HttpResponseRedirect(reverse('cart_homepage'))
    except prods.DoesNotExist:
        raise Http404
    
    # request.session.set_expiry(120000)
    # cart=None
    # try:
    #     the_id=request.session['cart_id']
    # except:
    #     new_cart=Cart()
    #     new_cart.save()

    #     request.session['cart_id']=new_cart.id
    #     the_id=new_cart.id
    # cart=Cart.objects.get(id=the_id)
    # print(cart)
    # cart=cart.objects.all()
    # try:
    #     prod=product.objects.get(slug=slug)
    # except prod.DoesNotExist:
    #     pass
    # except:
    #     pass
    # cart_item,created=CartItem.objects.get_or_create(cart=cart,product=prod)
    # if created:
    #     print("yes created cart")
        
    # new_totle=0.00
    # for item in cart_item.cart:
    #     new_totle += float(item.product.price)
    
    # request.session['items_totle']=cart_set.count()
    # cart.totle=new_totle
    # cart.save()
    # 
