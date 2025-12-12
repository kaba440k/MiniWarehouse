from django.contrib import admin

from inventory.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'storage',
        'quantity',
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'product',
        'storage',
        'created_at',
        'updated_at'
    ]
    search_fields = [
        'product',
        'storage',
    ]
    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    fieldsets = (
        ("Основная информация", {
            'fields': ('product', 'storage', 'quantity')
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
# Register your models here.
