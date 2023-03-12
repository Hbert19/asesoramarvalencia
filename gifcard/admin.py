from django.contrib import admin
from .models import Gifcard

class GifcardAdmin(admin.ModelAdmin):
    fields = (
        'date',
        'status'
    )

    list_display = (
        'code',
        'status',
        'status_payment',
        'email',
        'product'
    )

    search_fields = (
        'code',
        'email'
    )

    def has_add_permission(self, request):
        return False

admin.site.register(Gifcard, GifcardAdmin)
    
