from file_test_lessons import TestClass
from src.category import Category
from src.product import Product, Smartphone
import pytest




@pytest.fixture()
def product_one():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

@pytest.fixture()
def product_two():
    return Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1)

@pytest.fixture()
def product_tree():
    return Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)

@pytest.fixture
def firs_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        products=[Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3)])


@pytest.fixture()
def second_category():
    return Category(name= 'Техника',
                    description = "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                    products=([
                            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
                            Product("Nokia228", "5TB, Серый цвет, 999MP камера", 1800000.0, 1),
                            Product("MSI GF 76 Katana", "512GB, Черный цвет, 16gb ОЗУ, Win11", 79900, 3),
                            ]))


@pytest.fixture
def int_value_big():
    return 10000

@pytest.fixture
def int_value_small():
    return 0

@pytest.fixture
def product_samsung():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_tv(product_4):
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_4]
    )


@pytest.fixture
def category_smart(product_1, product_2, product_3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )


@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product_4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

@pytest.fixture
def product_prone():
    return Smartphone('Iphone', 'Б\У', 25000, 1, '-', 'XR', '128gb', 'pink')

@pytest.fixture
def test_file_test_class():
    return TestClass('Test')