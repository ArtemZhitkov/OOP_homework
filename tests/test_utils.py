import json
from unittest.mock import MagicMock, mock_open, patch

from src.utils import create_objects_from_json, read_json


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"name": "Смартфоны", "description": "Смартфоны, как средство не только '
    'коммуникации", "products": [{"name": "Samsung Galaxy C23 Ultra", '
    '"description": "256GB, Серый цвет, 200MP камера", "price": 180000.0, '
    '"quantity": 5}, {"name": "Iphone 15", "description": "512GB, Gray space", '
    '"price": 210000.0, "quantity": 8}]}]',
)
def test_read_json(mock_file, products_test) -> None:
    assert read_json(products_test) == [
        {
            "description": "Смартфоны, как средство не только коммуникации",
            "name": "Смартфоны",
            "products": [
                {
                    "description": "256GB, Серый цвет, 200MP камера",
                    "name": "Samsung Galaxy C23 Ultra",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"description": "512GB, Gray space", "name": "Iphone 15", "price": 210000.0, "quantity": 8},
            ],
        }
    ]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: MagicMock) -> None:
    result = read_json("../data/products.json")
    assert result == [{}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: MagicMock) -> None:
    assert read_json("../data/products.json") == [{}]


def test_create_objects_from_json(products_test) -> None:
    data = json.loads(products_test)
    result = create_objects_from_json(data)
    assert result[0].name == "Смартфоны"
