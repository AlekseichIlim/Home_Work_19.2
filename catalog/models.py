from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    picture = models.ImageField(upload_to='catalog/picture', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', **NULLABLE,
                                 related_name='product')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.name} - {self.category}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'price')


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.TextField(verbose_name='Содержимое')
    picture = models.ImageField(upload_to='catalog/blog/picture', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

