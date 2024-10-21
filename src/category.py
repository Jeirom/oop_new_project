from src.product import Product


class Category:
    """Этот класс 'Категории' принимает на вход значения ниже.
    Ведет подсчет количества категорий и уникальных продуктов"""

    name: str  # просто name
    description: str  # описание категории
    __products: list  # изменен статус на private
    category_count = 0  # кол-во категорий
    product_count = 0  # кол-во продуктов

    def __init__(self, name: str, description: str, products: list):
        """Передает значения в одноименные переменные,
        последние две строчки ведут счет количества категорий и уникальных продуктов"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> list:
        """Меняет значение атрибута на приватный"""
        return self.__products

    def add_product(self, new_product: Product) -> None:
        """Добавляет продукт в категорию"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        raise TypeError('Категории не совпадают')

    def __str__(self) -> str:
        """Маг-метод для выдачи юзеру информацию"""
        all_quantity = 0
        for j in self.__products:
            all_quantity += j.quantity
        return f"{self.name}, количество продуктов: {all_quantity} шт."
