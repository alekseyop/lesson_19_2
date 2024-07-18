import json

from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories(file_path='catalog/catalog_data.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [item for item in data if item['model'] == 'catalog.category']

    @staticmethod
    def json_read_products(file_path='catalog/catalog_data.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [item for item in data if item['model'] == 'catalog.product']

    def handle(self, *args, **kwargs):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        categories_for_create = []
        products_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for item in self.json_read_categories():
            fields = item['fields']
            category = Category(
                id=item['pk'],
                name=fields['name'],
                description=fields['description'],
            )
            categories_for_create.append(category)

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(categories_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for item in self.json_read_products():
            fields = item['fields']
            product = Product(
                id=item['pk'],
                name=fields['name'],
                description=fields.get('description', ''),
                image=fields.get('image', ''),
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
            )
            products_for_create.append(product)

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(products_for_create)

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
