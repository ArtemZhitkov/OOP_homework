from unittest.mock import MagicMock, mock_open, patch

from src.utils import create_objects_from_json, read_json

# @patch("src.utils.json.load")
# def test_read_json(mock: MagicMock, products_test: list[dict]) -> None:
#     mock.return_value = products_test
#     assert read_json('../data/products.json') == products_test


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: MagicMock) -> None:
    result = read_json("../data/products.json")
    assert result == [{}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: MagicMock) -> None:
    assert read_json("../data/products.json") == [{}]


def test_create_objects_from_json(products_test: list[dict]) -> None:
    result = create_objects_from_json(products_test)
    assert result[0].name == "Смартфоны"
