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

# def categories(request,id):
#     # cats=subcategory.objects.get(category=id)
#     prod=product.objects.filter(category=id)
#     contex={'Product':prod}
#     return render(request, 'shop/home.html',contex)

def single_product(request, slug):
    try:
        prods=product.objects.get(slug=slug)
        contex={'Product':prods}
        return render(request, 'shop/single_product.html',contex)
    except:
        raise Http404

