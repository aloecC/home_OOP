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
        self.__products.append(product)

    @property
    def products_list(self):
        products_info = []
        for product in self.__products:
            products_info.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_info


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Category.total_unique_products.add(name)

    def __len__(self):
        return self.quantity  # я не понимаю зачем тут len, если мы работаем по сути со счетчиком

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток на складе:{self.quantity} шт.'

    def __add__(self, other):
        return eval(f"{self.__price} * {self.quantity} + {other.__price} * {other.quantity}")

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


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, amount_of_built_in_memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.amount_of_built_in_memory = amount_of_built_in_memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, manufacturer_country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color
