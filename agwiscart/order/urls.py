from order import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.place_order, name='order_homepage'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('order-placed/', views.success_order, name='success_order'),
    path('deshboard/',views.deshboard,name='deshboard')
]
