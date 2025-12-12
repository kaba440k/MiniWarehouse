from django.contrib import admin

from storage.models import Storage


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'location',
            'is_active'
        ]
    list_filter = [
            'name',
            'location',
            'is_active'
        ]
    search_fields = [
            'name',
            'location',
        ]

# Register your models here.
