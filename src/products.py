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

    def add_product(self, product):
        """Метод добавляет продукт к списку продуктов в категории"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Метод возвращает строку с названием продукта его стоимость и остаток"""
        products_string = ""
        for product in self.__products:
            products_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_string


class Product:
    """Класс описывает название продукта, назначение, цену и количество продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict):
        """Метод добавляет новый продукт"""
        return cls(**product)

    @property
    def price(self):
        """Метод возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Метод позволяет изменить цену продукта"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(f"Подтвердите понижение цены c {self.__price} до {new_price}: y(да)/n(нет)\n").lower()
            if confirmation == "y":
                self.__price = new_price
        else:
            self.__price = new_price
