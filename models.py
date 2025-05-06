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
    """Represents a plate/meal containing multiple food products with quantities."""
    name: str
    products: dict[Product, float] = None

    def __post_init__(self):
        """Initialize products dictionary if not provided."""
        if self.products is None:
            self.products = {}
    
    def add_product(self, product: Product, quantity: float = 1.0) -> None:
        """Add a product to the plate.
        
        Args:
            product: Product to add
            quantity: Amount of product (default 1.0)
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.products[product] = self.products.get(product, 0) + quantity
    
    def total_calories(self) -> float:
        """Calculate total calories from all products on the plate accounting for quantities."""
        return sum(p.calories * q for p, q in self.products.items())
