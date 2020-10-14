from shop import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.all_product, name='shop_homepage'),
    path('cat/<id>/', views.categories, name='categorious_product'),
    path('scat/<id>/', views.subcategories, name='subcategorious_product'),
    path('s/<slug>/<sid>/', views.single_product, name='single_product'),
]
