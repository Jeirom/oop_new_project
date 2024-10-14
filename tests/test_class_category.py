def test_class_category(second_category,firs_category):
    assert second_category.name == "Техника"
    assert second_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert second_category.category_count == 2
    assert second_category.product_count == 4
    assert len(firs_category.products) == 1
