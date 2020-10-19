from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование товара')
    content = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True, verbose_name='Изображение товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Категория', db_index=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
