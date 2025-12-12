from django.db import models
from django.db.models import DO_NOTHING
from products.models import Product
from storage.models import Storage
from django.contrib.auth import get_user_model

User = get_user_model()

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name= 'Товар')
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT, verbose_name= 'Склад')
    type_CHOISES = (
        ('IN', 'Поступление'),
        ('OUT', 'Списание'),
        ('MOVE', 'Перемещение'),
        ('ADJUST', 'Настройка'),
    )
    type = models.CharField(max_length=20, choices=type_CHOISES, verbose_name='Тип действия', help_text='Тип действия')
    quantity = models.IntegerField(verbose_name='Изменение кол-ва')
    reference = models.CharField(max_length=255, verbose_name='Действие')
    created_by = models.ForeignKey(User, on_delete=DO_NOTHING, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product.name} на {self.storage.name} изменился на {self.quantity}"
# Create your models here.
