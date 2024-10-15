from src.product import Product


class Category:
    """Этот класс 'Категории' принимает на вход значения ниже.
    Ведет подсчет количества категорий и уникальных продуктов"""

    name: str
    description: str
    __products: list  # изменен статус на private
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Передает значения в одноименные переменные,
        последние две строчки ведут счет количества категорий и уникальных продуктов"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.product_count} шт.'
