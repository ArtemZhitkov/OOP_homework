def test_count_products_and_category(category) -> None:
    assert category.product_count == 4
    assert category.category_count == 1


def test_products(product) -> None:
    assert product.description == 'Я сама "вечность"'
    assert product.name == "Nokia 3310"
    assert product.price == 9.99
    assert product.quantity == 1
