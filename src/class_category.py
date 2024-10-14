class Category:
    """Этот класс 'Категории' принимает на вход значения ниже. Ведет подсчет количества категорий и уникальных продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Передает значения в одноименные переменные, последние две строчки ведут счет количества категорий и уникальных продуктов"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
