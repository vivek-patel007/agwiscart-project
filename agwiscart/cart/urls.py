from cart import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.carts, name='cart_homepage'),
    path('<slug>/<pid>/', views.update_cart, name='update_cart'),
    # path('<id>/', views.subcategories, name='subcategorious_product'),
    # path('single/<slug>/', views.single_product, name='single_product'),
]
