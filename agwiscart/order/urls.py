from order import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.place_order, name='order_homepage'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    # path('payment_done/', views.Payment_done, name='Payment_done'),
    # path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    # path('payment/', views.payment_request, name='pay'),
    # path('payment/', views.process_payment, name='pay'),
]
