from cart import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.carts, name='cart_homepage'),
    path('<slug>/<pid>/', views.update_cart, name='update_cart'),
    path('data/', views.get_cart_data, name='data'),
    path('update/', views.change_qnt, name='change_qnt'),
    # path('single/<slug>/', views.single_product, name='single_product'),
    # path('single/<slug>/', views.single_product, name='single_product'),
]
