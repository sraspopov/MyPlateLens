from __future__ import annotations
import csv
import sys
from dataclasses import dataclass
from loguru import logger

def configure_logging():
    logger.remove()  # Remove default handler
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )

@dataclass
class Product:
    name: str
    calories: float
    protein: float
    fat: float
    carbohydrates: float
    fiber: float
    sugar: float

@dataclass
class Plate:
    name: str
    products: list['Product'] = None

    def __post_init__(self):
        if self.products is None:
            self.products = []
    
    def add_product(self, product: 'Product'):
        self.products.append(product)
    
    def total_calories(self) -> float:
        return sum(p.calories for p in self.products)

class ProductDatabase:
    def __init__(self, csv_path='products.csv'):
        self.products = []
        self.load_products(csv_path)
    
    def load_products(self, csv_path):
        try:
            with open(csv_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    product = Product(
                    name=row['name'],
                    calories=float(row['calories']),
                    protein=float(row['protein']),
                    fat=float(row['fat']),
                    carbohydrates=float(row['carbohydrates']),
                    fiber=float(row['fiber']),
                    sugar=float(row['sugar'])
                    )
                    self.products.append(product)
                    logger.debug(f"Loaded product: {product.name}")
        except FileNotFoundError:
            logger.error(f"Products file not found at: {csv_path}")
            raise
        except (ValueError, KeyError) as e:
            logger.error(f"Error parsing CSV data: {e}")
            raise
    
    def get_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

def main():
    configure_logging()
    logger.info("Starting MyPlateLens application")
    db = ProductDatabase()
    
    # Example usage
    apple = db.get_product('Apple')
    banana = db.get_product('Banana')
    
    if apple and banana:
        breakfast = Plate("Breakfast")
        breakfast.add_product(apple)
        breakfast.add_product(banana)
        
        logger.info(f"Nutrition for {breakfast.name}:")
        logger.info(f"Total calories: {breakfast.total_calories():.1f}kcal")
        logger.info("Meal details:")
        for product in breakfast.products:
            logger.info(f"- {product.name}: {product.calories}kcal")

if __name__ == "__main__":
    main()
