import pytest

from src.category import Category


def test_class_category(second_category, firs_category):
    assert second_category.name == "Техника"
    assert (
        second_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert second_category.category_count == 2
    assert second_category.product_count == 4
    assert len(firs_category.products) == 1


def test_add_category(firs_category):
    assert Category.product_count == 5


def test_category_tv(category_tv, product_4):
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_tv.products == [product_4]


def test_category_smart(category_smart, product_1, product_2, product_3):
    assert category_smart.name == "Смартфоны"
    assert (
        category_smart.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smart.products == [product_1, product_2, product_3]


def test_category(category_smart, product_4):
    category_smart.add_product(product_4)
    assert Category.product_count == 13


def test_category_str(category_smart):
    assert str(category_smart) == "Смартфоны, количество продуктов: 27 шт."


def test_add_error(firs_category):
    with pytest.raises(TypeError):
        firs_category.add_product(1)
