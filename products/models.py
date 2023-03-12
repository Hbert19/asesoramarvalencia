from django.db import models

class Products(models.Model):
    name = models.CharField(verbose_name='Nombre del servicio', max_length=100)
    description = models.TextField(verbose_name='Descripción', blank=True, null=True)
    price = models.FloatField(verbose_name='Precio')
    image = models.FileField(verbose_name='Imagen del producto', blank=True, help_text='Tamaños recomendados: Desde 100x100 hasta 500x500 pixeles')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
