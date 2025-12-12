from rest_framework import serializers

from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    storage_name = serializers.CharField(source='storage.name', read_only=True)
    class Meta:
        model = Inventory
        fields = (
            'product',
            'product_name',
            'storage',
            'storage_name',
            'quantity',
            'updated_at'
        )
        read_only_fields = [
            'updated_at'
        ]