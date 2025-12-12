from django.db import models

class Storage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    location = models.CharField(max_length=255, verbose_name='Адрес')
    is_active = models.BooleanField(default=True, verbose_name='Статус активности')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['name']

    def __str__(self):
        return self.name
# Create your models here.
