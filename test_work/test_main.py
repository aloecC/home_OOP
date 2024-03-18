import pytest
from work.main import Category, Product


def test_category_initialization():
    """
    Проверяет корректность инициализации объектов класса Category
    """
    category = Category("Electronics", "Category for electronics")
    assert category.name == "Electronics"
    assert category.description == "Category for electronics"
    assert len(category.products) == 0


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
