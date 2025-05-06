from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    """Represents a food product with nutritional information."""
    name: str
    calories: float
    protein: float
    fat: float
    carbohydrates: float
    fiber: float
    sugar: float

@dataclass
class Plate:
    """Represents a plate/meal containing multiple food products."""
    name: str
    products: List[Product] = None

    def __post_init__(self):
        """Initialize products list if not provided."""
        if self.products is None:
            self.products = []
    
    def add_product(self, product: Product) -> None:
        """Add a product to the plate."""
        self.products.append(product)
    
    def total_calories(self) -> float:
        """Calculate total calories from all products on the plate."""
        return sum(p.calories for p in self.products)
