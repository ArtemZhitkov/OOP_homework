import json
import os

from src.products import Category, Product


def read_json(path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла, а возвращает список словарей с данными о продуктах"""
    full_path = os.path.abspath(path)
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            try:
                data: list[dict] = json.load(file)
                return data
            except json.JSONDecodeError:
                return [{}]
    except FileNotFoundError:
        return [{}]


def create_objects_from_json(data: list[dict]) -> list:
    """Функция принимает на вход список словарей и преобразовывает в список объектов класса"""

    products = []

    for item in data:
        products_list = []
        for product in item["products"]:
            products_list.append(Product(**product))
        item["products"] = products_list
        products.append(Category(**item))

    return products
