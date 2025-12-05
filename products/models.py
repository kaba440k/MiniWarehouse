from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True, verbose_name='Артикул')
    name = models.CharField(max_length=100, verbose_name='Имя')
    category = models.ManyToManyField(Category, related_name='products', blank=True, verbose_name='Категории')
    description = models.TextField(blank=True, verbose_name='Описание')
    min_stock = models.IntegerField(verbose_name= 'Мин. кол-во', help_text='Минимальное кол-во товаров для вызова уведомления')
    current_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Тек. цена')
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name[:50]
# Create your models here.
