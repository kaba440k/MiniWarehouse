from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'product',
            'storage',
            'type',
            'quantity',
            'reference',
            'created_by',
            'created_at',
        ]
        read_only_fields = [
            'created_by',
            'created_at',
        ]