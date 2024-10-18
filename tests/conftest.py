import json

import pytest

from src.products import Category, Product


@pytest.fixture
def product():
    return Product("Nokia 3310", 'Я сама "вечность"', 9.99, 1)


@pytest.fixture
def category():
    return Category(
        "Телефоны детства", "Вспомнить как было классно", ["Nokia 3310", "Motorola", "Siemens", "Sony Ericsson"]
    )


@pytest.fixture
def products_test():
    return json.dumps(
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                ],
            }
        ],
        ensure_ascii=False,
    )


@pytest.fixture
def category_test():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации",
        [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def new_product() -> dict:
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
