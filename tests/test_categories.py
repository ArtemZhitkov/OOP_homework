import pytest


def test_count_products_and_category(category, product) -> None:
    assert category.product_count == 4
    assert category.category_count == 1
    category.add_product(product)
    assert category.product_count == 5


def test_add_product_error(category):
    with pytest.raises(TypeError):
        category.add_product("product")


def test_category_property(category_test):
    assert category_test.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_iter_category(category_test):
    assert next(category_test) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(category_test) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    with pytest.raises(StopIteration):
        next(category_test)


def test_category_str(category_test):
    assert str(category_test) == "Смартфоны, количество продуктов: 13 шт."
