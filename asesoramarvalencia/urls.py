from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('woman/', views.woman_page, name='woman'),
    path('man/', views.man_page, name='man'),
    path('services/', views.online_services, name='services'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('contact/', views.contact, name='contact'),
    
    # Apps
    path('products/', include('products.urls')),
    path('pages/', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('gifcard/', include('gifcard.urls')),
    path('orders/', include('orders.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
