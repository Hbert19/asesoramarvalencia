from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('create-order/', views.create_order, name='create-order')
]