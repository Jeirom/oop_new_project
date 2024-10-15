from src.product import Product


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

