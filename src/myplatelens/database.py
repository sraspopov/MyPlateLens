import csv
from typing import Optional
from pathlib import Path
from loguru import logger
from myplatelens.models import Product

class ProductDatabase:
    """Handles loading and querying product nutritional data."""
    
    def __init__(self, csv_path: str = 'products.csv') -> None:
        """Initialize database with optional custom CSV path."""
        self.products: list[Product] = []
        self.load_products(csv_path)
    
    def load_products(self, csv_path: str) -> None:
        """Load products from CSV file into memory."""
        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
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
                    except (ValueError, KeyError) as e:
                        logger.warning(f"Skipping invalid product data: {e}")
                        continue
        except FileNotFoundError:
            logger.error(f"Products file not found at: {csv_path}")
            raise
    
    def get_product(self, name: str) -> Optional[Product]:
        """Find product by name (case-insensitive)."""
        return next(
            (p for p in self.products if p.name.lower() == name.lower()),
            None
        )
