from django.shortcuts import render
from django.http import JsonResponse
from .models import Products
from django.utils.html import strip_tags

def products(request):
    pass

def product_detail_view(request, id):
    product = Products.objects.get(pk=id)
    return render(request, 'product-detail-view.html', {
        "product": product,
        "product_description": product.description
    })


def get_product_price(request):
    id = request.POST.get('id')
    product = Products.objects.get(pk=id)
    return JsonResponse({
        "message": "success",
        "id": id,
        "price": product.price
    })
