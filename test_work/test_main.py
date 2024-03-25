import pytest
from work.main import Category, Product


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
    assert print(product) == 'Laptop, 1500.0 руб. Остаток на складе:10 шт.'


def test_string_display_category():
    category = Category("Electronics", "Category for electronics")
    product = Product("Laptop", "High-performance laptop", 1500, 10)
    category.add_product(product)
    assert print(category) == 'Electronics, количество продуктов: 1 шт.'


def test_food_addition():
    product_1 = Product("Laptop", "High-performance laptop", 1500.0, 10)
    product_2 = Product("Smartphone", "Latest smartphone model", 1000, 20)
    assert product_1 + product_2 == 35000.0
