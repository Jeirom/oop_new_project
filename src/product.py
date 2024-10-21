from itertools import product
from typing import Any

class Product:
    """Класс описания продуктов."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Передаются одноименные переменные, для дальнейшего использования как отдельно, так и в Category"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Меняет приватность атрибута прайс"""
        return self.__price

    @price.setter
    def price(self, value: int) -> None:
        """Меняет атрибут прайс на новое значение. Проводит проверку на цену"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: Any) -> Any:
        """Добавляет новый продукт"""
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        """Маг-метод для выдачи юзеру информацию"""
        return f"Название продукта: {self.name}, " f"Цена: {self.price} руб. " f"Остаток: {self.quantity} шт."

    def __repr__(self) -> str:
        """Маг-метод для отладки программы. Используется в разработке"""
        return (
            f"Product(name='{self.name}', description='{self.description}',"
            f" price={self.price}, quantity={self.quantity})"
        )

    def __add__(self, other: Any) -> float:
        """Маг-метод для подсчета всей суммы товаров на складе из цены * количество"""
        if type(other) == self.__class__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


class Smartphone(Product):

    name: str
    description: str
    price: float
    quantity: int
    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(self,name: str, description: str, price: float, quantity: int,efficiency,model,memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):

    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(self,name: str, description: str, price: float, quantity: int, country, germination_period, color):
        super().__init__(name, description, price,quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color






#
# test1 = Product('name', 'opis', 10000, 5)
#
# print(test1.name)
# print(test1.quantity)
# test2 = Smartphone('name','ope', 11111, 1, '1', '1', 1, 1)
# print(test2.memory)