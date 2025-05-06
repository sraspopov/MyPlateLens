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
    if apple:
        print(f"\nNutrition for {apple.name}:")
        print(f"Calories: {apple.calories}kcal")
        print(f"Protein: {apple.protein}g")
        print(f"Carbs: {apple.carbohydrates}g")

if __name__ == "__main__":
    main()
