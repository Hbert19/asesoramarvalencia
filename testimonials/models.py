from django.db import models

class Testimonial(models.Model):
    image = models.FileField(verbose_name='Imagen', blank=True, null=False, help_text='Tamaños recomendados: Desde 100x100 hasta 500x500 pixeles')
    name = models.CharField(max_length=100, verbose_name='Nombre del autor', null=True, blank=True)
    description = models.TextField(verbose_name='Testimonio', null=True, blank=True)
    date = models.DateField(verbose_name='Fecha', null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
