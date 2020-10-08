from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404,JsonResponse
from django.urls import reverse
from cart.models import UserCart
from shop.models import product
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
@login_required
def carts(request):
    cart=UserCart.objects.filter(owner__id=request.user.id)
    totle_item=cart.count()
    request.session['totle_item']=totle_item
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
def get_cart_data(request):
    items=UserCart.objects.filter(owner=request.user.id,payment_status=False)
    
    price,sell_price,quntity=0,0,0
    for i in items:
        price += int(i.product.price)*i.quantity
        sell_price +=float(i.product.sell_price)*i.quantity
        quntity += int(i.quantity)
       
        # totle +=float(i.product.sell_price)

    res={
        "price":price,"sell_price":sell_price,"quntity":quntity,
    }
    return JsonResponse(res)
def change_qnt(request):
    if "quantity" in request.GET:
        try:
            cid=request.GET.get('cid',None)
            quantity=request.GET.get('quantity',None)
            cart=get_object_or_404(UserCart,id=cid)
            cart.quantity=quantity
            cart.save()
            data={
                "cid":cid,
                 "quantity":quantity
            }
            return JsonResponse(data)
        except MultiValueDictKeyError:
            cid=False
            quantity=False
            return HttpResponseRedirect(reverse("cart_homepage"))
        # print(cid)
        # print(quantity)
        # cart=get_object_or_404(UserCart,id=cid)
        # cart.quantity=quantity
        # cart.save()