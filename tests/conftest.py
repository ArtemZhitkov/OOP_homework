import json

import pytest

from src.categories import Category
from src.lawngrass import LawnGrass
from src.products import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def smartphone1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
