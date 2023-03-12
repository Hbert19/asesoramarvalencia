from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime
import os
from asesoramarvalencia import settings
from products.models import Products
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from PIL import Image
from testimonials.models import Testimonial

class Home(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen 1', blank=True)
    header_image2 = models.FileField(verbose_name='Imagen 2', blank=True)
    header_image3 = models.FileField(verbose_name='Imagen 3', blank=True)
    header_title = models.CharField(verbose_name = 'Título del Header', max_length=100, blank=True)

    # Section 1
    section_1_title = models.CharField(max_length=100, verbose_name='Título', blank=True)
    section_1_description = models.TextField(verbose_name='Descripción', blank=True)
    section_1_image = models.FileField(verbose_name='Imagen', blank=True)

    # Section 2
    section_2_title = models.CharField(max_length=100, verbose_name='Título', blank=True)
    section_2_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 3
    section_3_title = models.CharField(max_length=100, verbose_name='Título', blank=True)
    section_3_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 4
    section_4_title = models.CharField(max_length=100, verbose_name='Título', blank=True)
    section_4_description = models.TextField(verbose_name='Descripción', blank=True)
    section_4_image = models.FileField(verbose_name='Imagen', blank=True)

    def __str__(self):
        return 'Página home'

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class About(models.Model):
    # Header
    header_image = models.FileField(verbose_name = 'Imagen', blank=True)
    header_title = models.CharField(verbose_name = 'Título del Header', max_length=100, blank=True)

    # Section 1
    section_1_title = models.CharField(verbose_name = 'Título', max_length=100, blank=True)
    section_1_subtitle = models.CharField(verbose_name = 'Subtítulo', max_length=100, blank=True)
    section_1_description = models.TextField(verbose_name = 'Drescripción', blank=True)
    section_1_image = models.FileField(verbose_name = 'Imagen', blank=True)

    # Testimonios
    testimonial_title = models.CharField(max_length=100, verbose_name='Título', blank=True)
    testimonial = models.ManyToManyField(Testimonial, verbose_name='Testimonios', blank=True)
    
    def __str__(self):
        return 'Página sobre mi'

    class Meta:
        verbose_name = 'Sobre mi'
        verbose_name_plural = 'Sobre mi'

class Woman(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen',blank=True)
    header_title = models.CharField(verbose_name='Título del Header', max_length=100, blank=True)

    # Section 1
    section_1_subtitle = models.CharField(verbose_name='Subtítulo', max_length=100, blank=True)
    section_1_title = models.CharField(verbose_name='Título', max_length=100, blank=True)
    section_1_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 2
    section_2_title = models.CharField(verbose_name='Título', blank=True, max_length=100)
    section_2_description = models.TextField(verbose_name='Descripción', blank=True)
    section_2_image = models.FileField(verbose_name='Imagen', blank=True)

    # Section 3
    section_3_title = models.CharField(verbose_name='Título', blank=True, max_length=100)
    section_3_description = models.TextField(verbose_name='Descripción', blank=True)

    def __str__(self) -> str:
        return 'Página mujeres'

    class Meta:
        verbose_name = 'Mujeres'
        verbose_name_plural = 'Mujeres'

class Man(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen',blank=True)
    header_title = models.CharField(verbose_name='Título del Header', max_length=100, blank=True)

    # Section 1
    section_1_title = models.CharField(verbose_name='Título', max_length=100, blank=True)
    section_1_description = models.TextField(verbose_name='Descripción', blank=True)
    section_1_image = models.FileField(verbose_name='Imagen', blank=True)

    # Section 2
    section_2_title = models.CharField(verbose_name='Título', blank=True, max_length=100)
    section_2_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 3
    section_3_title = models.CharField(verbose_name='Título', blank=True, max_length=100)
    section_3_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 4
    section_4_parallax = models.FileField(verbose_name='Imagen', blank=True)
    section_4_parallax_title = models.CharField(verbose_name='Título', blank=True, max_length=100)

    def __str__(self) -> str:
        return 'Página hombres'

    class Meta:
        verbose_name = 'Hombres'
        verbose_name_plural = 'Hombres'

class Services(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen',blank=True)
    header_title = models.CharField(verbose_name='Título del Header', max_length=100, blank=True)
    
    # Section 1
    section_1_title = models.CharField(verbose_name='Título', max_length=100, blank=True)
    section_1_description = models.TextField(verbose_name='Descripción', blank=True)

    # Section 2
    section_2_title = models.CharField(verbose_name='Título', max_length=100, blank=True)
    product = models.ManyToManyField(Products, blank=True)

    # Parallax
    section_3_parallax = models.FileField(verbose_name='Imagen', blank=True)
    section_3_parallax_title = models.CharField(verbose_name='Título', blank=True, max_length=100)




    def __str__(self) -> str:
        return 'Página servicios'

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'

class Gifcard(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen',blank=True)
    header_title = models.CharField(verbose_name='Título del Header', max_length=100, blank=True)

    def __str__(self) -> str:
        return 'Página Gifcard'
    
    class Meta:
        verbose_name = 'Gifcard'
        verbose_name_plural = 'Gifcard'

class Contact(models.Model):
    # Header
    header_image = models.FileField(verbose_name='Imagen',blank=True)
    header_title = models.CharField(verbose_name='Título del Header', max_length=100, blank=True)

    def __str__(self) -> str:
        return 'Página contacto'

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contacto'

# @receiver(post_save, sender=Home)
# def update_static(sender, **kwargs):
#     # Update staticfiles for update the template
#     subprocess.Popen(['python', 'manage.py', 'collectstatic', '--noinput'])
#     print('Updated')