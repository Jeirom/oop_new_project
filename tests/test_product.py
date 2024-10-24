from src.product import LawnGrass, Smartphone


def test_product_samsung(product_one):
    assert product_one.name == "Samsung Galaxy S23 Ultra"
    assert product_one.quantity == 5
    assert product_one.description == "256GB, Серый цвет, 200MP камера"
    assert product_one.price == 180000.0


def test_product_nokia(product_two):
    assert product_two.name == "Nokia228"
    assert product_two.quantity == 1
    assert product_two.description == "5TB, Серый цвет, 999MP камера"
    assert product_two.price == 1800000.0


def test_product_msi(product_tree):
    assert product_tree.name == "MSI GF 76 Katana"
    assert product_tree.quantity == 3
    assert product_tree.description == "512GB, Черный цвет, 16gb ОЗУ, Win11"
    assert product_tree.price == 79900


def test_product_str(product_two):
    assert str(product_two) == "Название продукта: Nokia228, Цена: 1800000.0 руб. Остаток: 1 шт."


def test_product_add(product_3, product_4):
    result = product_3 + product_4
    expected_result = (31000.0 * 14) + (123000.0 * 7)
    assert result == expected_result


def test_product_repr(product_two):
    assert repr(product_two) == (
        "Product(name='Nokia228', description='5TB," " Серый цвет, 999MP камера', price=1800000.0, quantity=1)"
    )


def test_add_prone_product(product_prone):
    assert product_prone.name == "Iphone"


def test_add_smartphone():
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    # grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    sum_product1 = smartphone1 + smartphone2
    assert sum_product1 == 2580000.0
