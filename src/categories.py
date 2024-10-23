from src.products import Product


class Category:
    """Класс описывает название категории и её описание. Подсчитывает количество
    продуктов в категории и количество категорий"""

    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products)
        Category.category_count += 1
        self.products_index = 0

    def __str__(self):
        """Магический метод возвращающий строковое отображение информации о количестве продуктов"""
        count_products = 0
        for product in self.__products:
            count_products += product.quantity
        return f"{self.name}, количество продуктов: {count_products} шт."

    def __iter__(self):
        self.products_index = 0
        return self

    def __next__(self):
        if self.products_index < len(self.__products):
            result = self.__products[self.products_index]
            self.products_index += 1
            return str(result)
        else:
            raise StopIteration

    def add_product(self, product):
        """Метод добавляет продукт к списку продуктов в категории"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Метод возвращает строку с названием продукта его стоимость и остаток"""
        products_string = ""
        for product in self.__products:
            products_string += f"{str(product)}\n"
        return products_string
