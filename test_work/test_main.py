import pytest
from work.main import Category, Product, Smartphone, LawnGrass


def test_category_initialization():
    """
    Проверяет корректность инициализации объектов класса Category
    """
    category = Category("Electronics", "Category for electronics")
    assert category.name == "Electronics"
    assert category.description == "Category for electronics"
    assert category.total_categories == 1


def test_product_initialization():
    """
    Проверяет корректность инициализации объектов класса Product
    """
    product = Product("Laptop", "Powerful laptop", 1500.55, 10)
    assert product.name == "Laptop"
    assert product.description == "Powerful laptop"
    assert product.price == 1500.55
    assert product.quantity == 10


def test_smartphone_initialization():
    smartphone = Smartphone('Iphone', 'technique', 85000, 15, '6 ядер', '12PRO', '128ГБ', "black")
    assert smartphone.name == "Iphone"
    assert smartphone.description == "technique"
    assert smartphone.price == 85000
    assert smartphone.quantity == 15
    assert smartphone.performance == '6 ядер'
    assert smartphone.model == '12PRO'
    assert smartphone.amount_of_built_in_memory == '128ГБ'
    assert smartphone.color == "black"


def test_lawn_grass_initialization():
    lawngrass = LawnGrass('short', 'for the dacha', 8000, 15, 'USA', '1 год', 'green')
    assert lawngrass.name == "short"
    assert lawngrass.description == 'for the dacha'
    assert lawngrass.price == 8000
    assert lawngrass.quantity == 15
    assert lawngrass.manufacturer_country == 'USA'
    assert lawngrass.germination_period == '1 год'
    assert lawngrass.color == 'green'


def test_category_and_product_counts():
    """
    Проверяет правильность подсчета количества категорий и продуктов
    """
    category1 = Category("Electronics", "Category for electronics")
    category2 = Category("Clothing", "Category for clothing")
    category3 = Category("Auto", "Category for Auto")

    product1 = Product("Laptop", "Powerful laptop", 1500.55, 10)
    product2 = Product("T-shirt", "Cotton T-shirt", 20.99, 30)

    assert Category.total_categories == 4
    assert len(Category.total_unique_products) == 2


def test_category_add_product():
    category = Category("Electronics", "Category for electronic devices")
    product = Product("Laptop", "High-performance laptop", 1500, 10)
    category.add_product(product)
    assert len(category.products_list) == 1
    assert category.products_list[0] == "Laptop, 1500 руб. Остаток: 10 шт."


def test_product_creation():
    product = Product("Smartphone", "Latest smartphone model", 1000, 20)
    assert product.name == "Smartphone"


def test_price_setter_increase():
    product = Product("Laptop", "High-performance laptop", 1500.0, 10)
    product.price = 1600.0
    assert product.price == 1600.0

    product.price = -100.0
    assert product.price == 1600.0


def test_string_display_product():
    product = Product("Laptop", "High-performance laptop", 1500.0, 10)
    assert str(product) == 'Laptop, 1500.0 руб. Остаток на складе:10 шт.'


def test_string_display_category():
    category = Category("Electronics", "Category for electronics")
    product = Product("Laptop", "High-performance laptop", 1500, 10)
    category.add_product(product)
    assert str(category) == 'Electronics, количество продуктов: 1 шт.'


def test_food_addition():
    product_1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
    product_2 = Product("Smartphone", "Latest smartphone model", 1000, 20)
    assert product_1 + product_2 == 35000.0


def test_new_product():
    lawn_grass1 = LawnGrass('Трава1', 'Описание травы', 20, 100, 'Country A', '2 weeks', 'Green')
    print(lawn_grass1) == 'Создан объект класса LawnGrass\nС атрибутами:name=Трава1, description=Описание травы, _Product__price=20, quantity=100, manufacturer_country=Country A, germination_period=2 weeks, color=Green'
    smartphone1 = Smartphone('Смартфон1', 'Описание смартфона', 1000, 5, 'High', 'Model X', '64GB', 'Black')
    print(smartphone1) == 'Создан объект класса Smartphone\nС атрибутами:name=Смартфон1, description=Описание смартфона, _Product__price=1000, quantity=5, performance=High, model=Model X, amount_of_built_in_memory=64GB, color=Black'