from django.contrib import admin

from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # Настройка админ-панели
    list_display = [
            'product',
            'storage',
            'type',
            'quantity',
            'reference',
            'created_by',
            'created_at',
        ]
    list_filter = [
        'product',
        'storage',
        'type',
        'quantity',
        'reference',
        'created_by',
        'created_at',
    ]
    search_fields = [
        'product',
        'storage',
        'type',
        'reference',
        'created_by',
        'created_at',]
    readonly_fields = ['created_by','created_at']
    list_select_related = ('product', 'storage', 'created_by')
    fieldsets = (
        ("Основная информация", {
            'fields': ('product', 'storage',)
        }),
        ("Действие", {
            'fields': ('type', 'quantity', 'reference',)
        }),
        ('Временные метки', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        })
    )
    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


# Register your models here.
