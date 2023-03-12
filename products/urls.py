from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product-view/<int:id>', views.product_detail_view, name='product-detail-view'),
    path('get-price/', views.get_product_price, name='get-product-price')
]