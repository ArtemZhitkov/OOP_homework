from unittest.mock import patch

import pytest

from src.products import Product


def test_count_products_and_category(category, product) -> None:
    assert category.product_count == 4
    assert category.category_count == 1
    category.add_product(product)
    assert category.product_count == 5


def test_products(product) -> None:
    assert product.description == 'Я сама "вечность"'
    assert product.name == "Nokia 3310"
    assert product.price == 9.99
    assert product.quantity == 1
    assert str(product) == "Nokia 3310, 9.99 руб. Остаток: 1 шт."


def test_category_property(category_test):
    assert category_test.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_new_product(new_product):
    result = Product.new_product(new_product)
    assert result.name == "Samsung Galaxy C23 Ultra"
    assert result.description == "256GB, Серый цвет, 200MP камера"
    assert result.price == 180000.0
    assert result.quantity == 5


def test_new_price(product):
    product.price = 100.0
    assert product.price == 100


def test_new_price_negative(capsys, product):
    product.price = -1
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


@patch("builtins.input", side_effect="y")
def test_new_price_low(mock, product):
    product.price = 5
    assert product.price == 5


def test_iter_category(category_test):
    assert next(category_test) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(category_test) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    with pytest.raises(StopIteration):
        next(category_test)


def test_category_str(category_test):
    assert str(category_test) == "Смартфоны, количество продуктов: 13 шт."


def test_add(product2, product3):
    assert product2 + product3 == 2580000.0
