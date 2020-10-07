from django.shortcuts import render,Http404,get_object_or_404
from django.http import HttpResponse
from shop.models import product,productimages,category,subcategory
def all_product(request):
    prod=product.objects.all()
    cat=subcategory.objects.all()
    contex={'Product':prod,'cat':cat}
    return render(request, 'shop/home.html',contex)

def subcategories(request,id):
    cats=subcategory.objects.get(subcategory_id=id)
    prod=product.objects.filter(subcategory=cats)
    contex={'Product':prod}
    return render(request, 'shop/home.html',contex)

def categories(request,id):
    cats=category.objects.get(category_id=id)
    prod=product.objects.filter(category=cats)
    contex={'Product':prod}
    return render(request, 'shop/home.html',contex)

def single_product(request, slug, sid):
    # try:
    prods=product.objects.get(slug=slug)
    rel=product.objects.filter(subcategory=sid)
    contex={'Product':prods,'rel':rel}
    return render(request, 'shop/single_product.html',contex)
    # except:
    #     raise Http404

