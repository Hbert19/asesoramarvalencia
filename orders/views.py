from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Order
from products.models import Products

def orders(request):
    return HttpResponse('Works!')

def create_order(request):
    id = request.POST.get('id')
    product = Products.objects.get(pk=id)
    order = Order.objects.create(product=product)
    order.save()
    return JsonResponse({
        'message': 'created',
        'order': order.id
    })
