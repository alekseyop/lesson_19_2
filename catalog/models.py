from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:  # метаданные
        verbose_name = 'Категория'  # наименование в единственном числе
        verbose_name_plural = 'Категории'  # наименование во множественном числе


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение (превью)", **NULLABLE)  # изображение
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    # manufactured_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата производства продукта")

    def __str__(self):
        return f"{self.name} ({self.category.name})"  # возвращает название товара и название категории

    class Meta:  # метаданные товара
        verbose_name = 'Товар'  # наименование в единственном числе товара
        verbose_name_plural = 'Товары'  # наименование во множественном числе товара
        ordering = ['-created_at']  # сортировка по дате создания в порядке убывания (по возрастанию)
        # ordering = ['-updated_at']  # сортировка по дате последнего изменения в порядке убывания (по убыванию)
