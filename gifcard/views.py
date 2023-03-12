from django.shortcuts import render
from products.models import Products
from .models import Gifcard
from django.http import JsonResponse
from datetime import datetime
from orders.models import Order
from django.http import Http404
from pages.models import Gifcard as GifcardPage
from asesoramarvalencia.utils import SendEmail
from django.template.loader import render_to_string

def gifcard(request):
    products = Products.objects.all()
    gifcard = GifcardPage.objects.all().first()
    return render(request, 'gifcard.html', {
        "products": products,
        "gifcard": gifcard
    })

def create_gifcard(request):
    id = request.POST.get('id')
    email = request.POST.get('email')
    product = Products.objects.get(pk=id)
    gifcard = Gifcard.objects.create(product = product, date=datetime.now(), email=email)
    gifcard.save()
    html_message = render_to_string('gifcard-email.html', {
        "gifcard": gifcard
    })

    SendEmail(request, 'Código Gifcard', html_message, [email]).send()

    return JsonResponse({
        "message": "created",
        "product_price": product.price,
        "gifcard_email": gifcard.email
    })

def redeem_gifcard(request):
    if request.method == 'POST':
        code = request.POST.get('gifcard')
        product_id = request.POST.get('productId')
        gifcard = Gifcard.objects.filter(code=code).first()
        try:
            gifcard.check_gifcard()
        except AttributeError:
            return JsonResponse({
                "error": "El código de tu gifcard no es válido"
            })
        product = Products.objects.get(pk=product_id)
        if gifcard.check_gifcard():
            if gifcard.product == product:
                order = Order.objects.create(product=gifcard.product)
                gifcard.status = True
                gifcard.save()
                return JsonResponse({
                    'success': 'Compra realizada correctamente tu número de orden es {}'.format(order.id),
                    "order": order.id
                })
            
            return JsonResponse({
                "error": "Esta gifcard solo es válida para {}".format(gifcard.product)
            })
        
        return JsonResponse({
            "error": "El código de tu gifcard no es válido"
        })
    raise Http404()