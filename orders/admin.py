from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'product',
        'status'
    )

    search_fields = (
        'id',
    )

    def has_add_permission(self, request) -> bool:
        return False

admin.site.register(Order, OrderAdmin)
