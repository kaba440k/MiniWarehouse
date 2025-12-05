from django.contrib import admin
from .models import Product, Category


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Настройка админ-панели
    list_display = ['sku', 'name', 'display_categories', 'description', 'min_stock', 'current_price', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active','created_at', 'updated_at']
    search_fields = ['sku','name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ("Основная информация", {
            'fields': ('sku', 'name', 'category', 'description')
        }),
        ("Цена и запас", {
            'fields': ('current_price', 'min_stock')
        }),
        ("Статус", {
            'fields': ('is_active',)
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def display_categories(self, obj):
        """Отображает категории через запятую"""
        return ", ".join([cat.name for cat in obj.category.all()])

    display_categories.short_description = "Категории"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    # fieldsets = ("Название категории", {'fields' : 'name'})