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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Метод возвращает строку с названием продукта его стоимость и остаток"""
        products_string = ""
        for product in self.__products:
            products_string += f"{str(product)}\n"
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

    def __str__(self):
        """Магический метод возвращающий строковое отображение информации о стоимости и количестве продукта"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Магический метод возвращает сумму цен двух товаров"""
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, dict_product: dict, products=None):
        """Метод добавляет новый продукт"""
        if products:
            for product in products:
                if product.name == dict_product["name"]:
                    product.quantity += dict_product["quantity"]
                    product.price = max([product.price, product["price"]])
                    return product
        return cls(**dict_product)

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
