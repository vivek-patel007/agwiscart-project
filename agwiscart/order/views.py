from django.shortcuts import render,reverse,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from order.models import UserOrder
from cart.models import UserCart
from django.contrib.auth.models import User
from PayTm import Checksum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def place_order(request):
    if request.method=='POST':
       fname=request.POST["fname"]
       lname=request.POST["lname"]
       state=request.POST["state"]
       add=request.POST["add"]
       add2=request.POST["add2"]
       city=request.POST["city"]
       zipc=request.POST["zipc"]
       phone=request.POST["phone"]
       mail=request.POST["mail"]
       am=request.POST['amount']

       amt=int(float(am))

       
    
            
       if fname=="" or lname=="" or state=="" or add=="" or city=="" or zip=="" or len(zipc)<6 or phone=="" or mail=="":
            messages.error(request,"please fill up the all details")
       else:
            crt=UserCart.objects.filter(owner=request.user.id,payment_status=False)
            product=""
            inv="INV-"
            cart_ids=""
            for i in crt:
                product+=str(i.product.product_id)+","
                inv+= str(i.id)+","+str(i.product_id)
                cart_ids+=str(i.id)+","

            usr=User.objects.get(id=request.user.id)
            ordr=UserOrder(owner=usr,cart_ids=cart_ids,product_ids=product,invoice_id=inv,first_name=fname,last_name=lname,state=state,address=add,address2=add2,city=city,zip_code=zipc,phone=phone,email=mail,amount=amt)
            ordr.save()
            request.session["order_id"]=ordr.order_id
            
            
          
            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount':ordr.amount,
                'item_name': 'Order {}'.format(ordr.product_ids),
                'invoice': str(inv),
                'currency_code': 'INR',
                'notify_url': 'http://{}{}'.format('127.0.0.1:8000',
                                                   reverse('paypal-ipn')),
                'return_url': 'http://{}{}'.format('127.0.0.1:8000',
                                                   reverse('payment_done')),
                'cancel_return': 'http://{}{}'.format('127.0.0.1:8000',
                                                      reverse('payment_cancelled')),
            }
           

            form = PayPalPaymentsForm(initial=paypal_dict)
            return render(request, 'order/process_payment.html', {'order': ordr, 'form': form})
    return render(request,'order/checkout.html')
@csrf_exempt
def payment_done(request):
    if "order_id" in request.session:
        order_id=request.session["order_id"]
        ord_obj=get_object_or_404(UserOrder,order_id=order_id)
        ord_obj.payment_status=True
        ord_obj.save()
        for i in ord_obj.cart_ids.split(","):
            crt=UserCart.objects.get(id=i)
            crt.payment_status=True
            crt.save()
    return render(request, 'order/payment_done.html')


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'order/payment_cancelled.html')