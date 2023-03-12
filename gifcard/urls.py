from django.urls import path
from . import views

urlpatterns = [
    path('', views.gifcard, name='gifcard'),
    path('create-gifcard/', views.create_gifcard, name='create-gifcard'),
    path('redeem/', views.redeem_gifcard, name='apply-gifcard')
]