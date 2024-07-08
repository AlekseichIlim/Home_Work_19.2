import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("category_data.json", encoding='utf8') as file:
            categories = json.load(file)
            return categories

    @staticmethod
    def json_read_products():
        with open("product_data.json", encoding='utf8') as file:
            products = json.load(file)
            return products

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category['pk'],
                    name=category['fields']['name'],
                    description=category['fields']['description'])
            )
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продукты из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product['pk'],
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    picture=product['fields']['picture'],
                    category=Category.objects.get(pk=product['fields']['category']),
                    price=product['fields']['price'],
                    created_at=product['fields']['created_at'],
                    updated_at=product['fields']['updated_at'])
            )
        Product.objects.bulk_create(product_for_create)
