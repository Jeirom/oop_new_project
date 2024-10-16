from src.product import Product


class Category:
    """Этот класс 'Категории' принимает на вход значения ниже.
    Ведет подсчет количества категорий и уникальных продуктов"""

    name: str
    description: str
    __products: list  # изменен статус на private
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, __products: list):
        """Передает значения в одноименные переменные,
        последние две строчки ведут счет количества категорий и уникальных продуктов"""
        self.name = name
        self.description = description
        self.__products = __products
        Category.category_count += 1
        Category.product_count += len(__products)

    @property
    def products(self):
        return self.__products

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def product_list(self):
        product_str = ""
        for product in self.products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str
