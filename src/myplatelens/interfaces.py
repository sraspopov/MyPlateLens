from abc import ABC, abstractmethod
from typing import Optional
from myplatelens.models import Product

class IProductDatabase(ABC):
    """Abstract base class for product database implementations."""
    
    @abstractmethod
    def get_product(self, name: str) -> Optional[Product]:
        """Retrieve product by name."""
        pass

    @abstractmethod
    def add_product(self, product: Product) -> None:
        """Add a new product to the database."""
        pass

    @abstractmethod
    def load_products(self, source: str) -> None:
        """Load products from data source."""
        pass
