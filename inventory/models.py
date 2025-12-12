from django.db import models
from products.models import Product
from storage.models import Storage


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT, verbose_name='Склад')
    quantity = models.IntegerField(default=0, verbose_name = 'Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Остаток'
        verbose_name_plural = 'Остатки'
        unique_together = [['product', 'storage']]

    def __str__(self):
        return f"{self.product.name} на {self.storage.name}: {self.quantity}"
# Create your models here.
