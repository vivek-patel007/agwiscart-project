from django.shortcuts import render,Http404,get_object_or_404
from django.http import HttpResponse
from shop.models import product,productimages,category,subcategory
# from django.urls import reverse
# Create your views here.
def all_product(request):
    prod=product.objects.all()
    contex={
        'Product':prod
    }
    return render(request, 'shop/home.html',contex)

def categories(request,id):
    scats=subcategory.objects.get(subcategory_id=id)
    prod=product.objects.filter(subcategory=scats)
    contex={
        'Product':prod
    }
    return render(request, 'shop/home.html',contex)

def single_product(request, slug):
    # try:
    prods=product.objects.get(slug=slug)
    # print(slug)
    # print(prods.title)
    contex={'Product':prods}
    return render(request, 'shop/single_product.html',contex)
    # except:
    #     raise Http404

