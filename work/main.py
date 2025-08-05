from abc import ABC, abstractmethod


class InfoMixin:
    def __repr__(self):
        attr_list = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"Создан объект класса {self.__class__.__name__}\nС атрибутами:{', '.join(attr_list)}"

    def show_info(self):
        info = f"Название: {self.name}\nОписание: {self.description}\nЦена: {self.price}\nКоличество: {self.quantity}"
        return info


class Category:
    name: str
    description: str
    goods: str

    total_categories = 0
    total_unique_products = set()

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        return len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product) or issubclass(type(product), Product):
            self.__products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    @property
    def products_list(self):
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_info

class ProductABC(ABC):
    @abstractmethod
    def get_info(self):
        pass

class Product(ProductABC):
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Category.total_unique_products.add(name)

    def __len__(self):
        return self.quantity

    # def __str__(self):
    # return f'{self.name}, {self.__price} руб. Остаток на складе:{self.quantity} шт.'

    def __add__(self, other):
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError("Нельзя складывать товары разных классов")

    @staticmethod
    def create_new_product(name, description, price, quantity):
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                confirmation = input("Вы уверены, что хотите понизить цену? (yes/no): ")
                if confirmation.lower() == "yes":
                    self.__price = new_price
                    print("Цена успешно изменена.")
                else:
                    print("Действие отменено.")
            else:
                self.__price = new_price
                print("Цена успешно изменена.")
        else:
            print("Ошибка: Цена введена некорректно.")


class Smartphone(Product, InfoMixin):
    def __init__(self, name, description, price, quantity, performance, model, amount_of_built_in_memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.amount_of_built_in_memory = amount_of_built_in_memory
        self.color = color


    def get_info(self):
        return f"{super().show_info()}\nПроизводительность: {self.performance}\nМодель: {self.model}\nОбъем встроенной памяти: {self.amount_of_built_in_memory}\nЦвет: {self.color}"


class LawnGrass(Product, InfoMixin):
    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color


    def get_info(self):
        return f"{super().show_info()}\nСтрана производитель: {self.manufacturer_country}\nПериод прорастания: {self.germination_period}\nЦвет: {self.color}"


class OrderableItem(ABC):
    def __init__(self, item_link, item_quantity, total_price):
        self.item_link = item_link
        self.item_quantity = item_quantity
        self.total_price = total_price

    @abstractmethod
    def __str__(self):
        pass

class Order(OrderableItem):
    def __str__(self):
        return f'Заказ: {self.item_link}\nКоличество: {self.item_quantity}\nИтоговая стоимость: {self.total_price}'

''