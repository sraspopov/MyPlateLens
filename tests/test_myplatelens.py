import pytest
from pathlib import Path
import csv
from myplatelens.models import Product, Plate
from myplatelens.database import ProductDatabase

@pytest.fixture
def sample_product() -> Product:
    """Fixture providing a sample Product for testing."""
    return Product(
        name="Test Product",
        calories=100.0,
        protein=5.0,
        fat=2.0,
        carbohydrates=20.0,
        fiber=3.0,
        sugar=10.0
    )

@pytest.fixture
def sample_plate(sample_product) -> Plate:
    """Fixture providing a sample Plate with one product for testing."""
    plate = Plate("Test Plate")
    plate.add_product(sample_product)
    return plate

@pytest.fixture
def temp_csv(tmp_path: Path) -> Path:
    """Fixture creating a temporary CSV file with test product data."""
    csv_path = tmp_path / "test_products.csv"
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'name', 'calories', 'protein', 'fat', 
            'carbohydrates', 'fiber', 'sugar'
        ])
        writer.writeheader()
        writer.writerow({
            'name': 'Test Apple',
            'calories': '52',
            'protein': '0.3',
            'fat': '0.2',
            'carbohydrates': '14',
            'fiber': '2.4',
            'sugar': '10'
        })
    return csv_path

def test_product_creation(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.calories == 100.0
    assert sample_product.protein == 5.0
    assert sample_product.fat == 2.0
    assert sample_product.carbohydrates == 20.0
    assert sample_product.fiber == 3.0
    assert sample_product.sugar == 10.0

def test_plate_operations(sample_plate, sample_product):
    assert sample_plate.name == "Test Plate"
    assert len(sample_plate.products) == 1
    assert sample_product in sample_plate.products
    assert sample_plate.products[sample_product] == 1.0
    assert sample_plate.total_calories() == 100.0

def test_product_database_load(temp_csv):
    db = ProductDatabase(temp_csv)
    assert len(db.products) == 1
    apple = db.get_product('Test Apple')
    assert apple is not None
    assert apple.name == 'Test Apple'
    assert apple.calories == 52.0
    assert apple.protein == 0.3

def test_product_database_missing_product(temp_csv):
    db = ProductDatabase(temp_csv)
    assert db.get_product('Nonexistent') is None

def test_plate_total_calories_with_multiple_products(sample_plate, sample_product):
    # Add another product
    another_product = Product(
        name="Another Product",
        calories=200.0,
        protein=10.0,
        fat=4.0,
        carbohydrates=40.0,
        fiber=6.0,
        sugar=20.0
    )
    sample_plate.add_product(another_product, 2.0)  # Add 2 units
    # Original product (100kcal) + 2 units of new product (200kcal * 2)
    assert sample_plate.total_calories() == 500.0
