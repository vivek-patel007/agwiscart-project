from django.shortcuts import render,reverse
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from order.models import Order
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
       amt=request.POST['amount']
       print(fname)
        # lname,state,add,add2,city,zipc,phone,mail,1.00)
            
       if fname=="" or lname=="" or state=="" or add=="" or city=="" or zip=="" or phone=="" or mail=="":
            messages.error(request,"please fill up the all details")
       if len(zipc)<6:
           messages.error(request,"please enter valid zip code...")
       else:
            ordr=Order(first_name=fname,last_name=lname,state=state,address=add,address2=add2,city=city,zip_code=zipc,phone=phone,email=mail,amount=amt)
            ordr.save()
            # messages.success(request,"your order place success")
            paypal_dict = {
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'amount':ordr.amount,
                'item_name': 'Order {}'.format(ordr.cart),
                'invoice': str(ordr.order_id),
                'currency_code': 'INR',
                'notify_url': 'http://{}{}'.format('127.0.0.1:800',
                                                   reverse('paypal-ipn')),
                # 'return_url': 'http://{}{}'.format(host,
                #                                    reverse('payment_done')),
                # 'cancel_return': 'http://{}{}'.format(host,
                                                    #   reverse('payment_cancelled')),
            }

                # paypal_dict = {
                #     'business': settings.PAYPAL_RECEIVER_EMAIL,
                #     'amount': '%.2f' % order.total_cost().quantize(
                #         Decimal('.01')),
                #     'item_name': 'Order {}'.format(order.id),
                #     'invoice': str(order.id),
                #     'currency_code': 'USD',
                #     'notify_url': 'http://{}{}'.format(host,
                #                                        reverse('paypal-ipn')),
                #     'return_url': 'http://{}{}'.format(host,
                #                                        reverse('payment_done')),
                #     'cancel_return': 'http://{}{}'.format(host,
                #                                           reverse('payment_cancelled')),
                # }

            form = PayPalPaymentsForm(initial=paypal_dict)
            return render(request, 'order/process_payment.html', {'order': ordr, 'form': form})
    return render(request,'order/checkout.html')
@csrf_exempt
def payment_done(request):
    return render(request, 'order/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'order/payment_cancelled.html')