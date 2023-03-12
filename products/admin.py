from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Products

class ProductAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Products, ProductAdmin)
