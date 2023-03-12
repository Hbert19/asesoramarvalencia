from django.contrib import admin
from .models import Home, About, Woman, Man, Services, Contact, Gifcard
from django.contrib.auth.models import User, Group
from django.db import models
from tinymce.widgets import TinyMCE
from testimonials.models import Testimonial

class HomeAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_image2', 'header_image3', 'header_title',),
        }),
        ('Sección 1', {
            'fields': ('section_1_title', 'section_1_description', 'section_1_image'),
        }),
        ('Sección 2', {
            'fields': ('section_2_title', 'section_2_description'),
        }),
        ('Sección 3', {
            'fields': ('section_3_title', 'section_3_description'),
        }),
        ('Sección 4', {
            'fields': ('section_4_title', 'section_4_description', 'section_4_image'),
        }),
    )

    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class AboutAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title'),
        }),
        ('Sección 1', {
            'fields': ('section_1_title', 'section_1_subtitle', 'section_1_description', 'section_1_image'),
        }),
        ('Testimonios', {
            'fields': ('testimonial_title', 'testimonial'),
        }),
    )

    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class WomanAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title')
        }),
        ('Sección 1', {
            'fields': ('section_1_subtitle', 'section_1_title', 'section_1_description')
        }),
        ('Sección 2', {
            'fields': ('section_2_title', 'section_2_description', 'section_2_image')
        }),
        ('Sección 3', {
            'fields': ('section_3_title', 'section_3_description')
        })
    )

    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class ManAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title')
        }),
        ('Sección 1', {
            'fields': ('section_1_title', 'section_1_description', 'section_1_image')
        }),
        ('Sección 2', {
            'fields': ('section_2_title', 'section_2_description')
        }),
        ('Sección 3', {
            'fields': ('section_3_title', 'section_3_description')
        }),
        ('Parallax', {
            'fields': ('section_4_parallax', 'section_4_parallax_title')
        })
    )

    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class ServicesAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title')
        }),
        ('Sección 1', {
            'fields': ('section_1_title', 'section_1_description')
        }),
        ('Sección 2', {
            'fields': ('section_2_title', 'product')
        }),
        ('Parallax', {
            'fields': ('section_3_parallax', 'section_3_parallax_title')
        })
    )
    
    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class GifcardAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title')
        }),
    )

    def has_add_permission(self, request):
        return False
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Header', {
            'fields': ('header_image', 'header_title')
        }),
    )

    def has_add_permission(self, request):
        return False    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Home, HomeAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Woman, WomanAdmin)
admin.site.register(Man, ManAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Gifcard, GifcardAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.unregister([User, Group])
