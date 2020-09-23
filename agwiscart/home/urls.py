from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contactpage'),
    path('about/', views.about, name='aboutpage'),
    path('login/', views.loginhandle, name='loginpage'),
    path('logout/', views.logouthandle, name='logout'),
    path('signup/', views.signuphandle, name='signuphandle'),
]
