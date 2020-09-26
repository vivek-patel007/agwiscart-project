from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def all_product(request):
    return HttpResponse("<h1>shop</h1><br><a href="">second</a>")
def single_product(request):
    return HttpResponse("<h1><a href="">second</a></h1>")