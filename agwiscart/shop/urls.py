from shop import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.all_product, name='all_product'),
    path('single/', views.single_product, name='single_product'),
]
