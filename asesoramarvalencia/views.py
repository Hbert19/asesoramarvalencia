from django.shortcuts import render
from django.http import JsonResponse
from pages.models import Home, About, Woman, Man, Services, Contact
from django.template.loader import render_to_string
from .utils import SendEmail

def index(request):
    home = Home.objects.all().first()
    return render(request, 'index.html', {
        "home": home
    })

def about(request):
    about = About.objects.all().first()
    return render(request, 'about.html', {
        "about": about
    })

def woman_page(request):
    woman = Woman.objects.all().first()
    return render(request, 'woman.html', {
        "woman": woman
    })

def man_page(request):
    man = Man.objects.all().first()
    return render(request, 'man.html', {
        "man": man
    })

def online_services(request):
    service = Services.objects.all().first()
    return render(request, 'services.html', {
        "service": service
    })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        html_message = render_to_string('contact-email.html', {
            "name": name,
            "email": email,
            "message": message
        })

        SendEmail(request, 'Consulta cliente', html_message, ['mardelval.9@gmail.com']).send()

        return JsonResponse({
            'success': True
        })
    
    contact = Contact.objects.all().first()

    return render(request, 'contact.html', {
        "contact": contact
    })

def privacy_policy(request):
    return render(request, 'privacy-policy.html', {

    })