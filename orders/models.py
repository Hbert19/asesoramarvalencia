from django.db import models
import uuid
from products.models import Products

class Order(models.Model):
    id = models.UUIDField(verbose_name='ID de la orden', default=uuid.uuid4, primary_key=True, editable=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Producto')
    status = models.BooleanField(verbose_name='Estado de pago', default=True)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
