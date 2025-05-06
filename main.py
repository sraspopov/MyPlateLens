from __future__ import annotations
import csv
from dataclasses import dataclass

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
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.products.append(Product(
                    name=row['name'],
                    calories=float(row['calories']),
                    protein=float(row['protein']),
                    fat=float(row['fat']),
                    carbohydrates=float(row['carbohydrates']),
                    fiber=float(row['fiber']),
                    sugar=float(row['sugar'])
                ))
    
    def get_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

def main():
    print("Welcome to MyPlateLens!")
    db = ProductDatabase()
    
    # Example usage
    apple = db.get_product('Apple')
    banana = db.get_product('Banana')
    
    if apple and banana:
        breakfast = Plate("Breakfast")
        breakfast.add_product(apple)
        breakfast.add_product(banana)
        
        print(f"\nNutrition for {breakfast.name}:")
        print(f"Total calories: {breakfast.total_calories():.1f}kcal")
        print("\nDetails:")
        for product in breakfast.products:
            print(f"- {product.name}: {product.calories}kcal")

if __name__ == "__main__":
    main()
