from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    display_categories = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
                  'id',
                  'sku',
                  'name',
                  'display_categories',
                  'description',
                  'min_stock',
                  'current_price',
                  'is_active',
                  'created_at',
                  'updated_at',
                  )
        read_only_fields = [
            'created_at',
            'updated_at'
        ]

    def get_display_categories(self, obj):
        """Отображает категории через запятую"""
        return ", ".join([cat.name for cat in obj.category.all()])

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']