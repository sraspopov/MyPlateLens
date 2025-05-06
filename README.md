# MyPlateLens

MyPlateLens is a simple nutrition tracking application that helps you calculate the nutritional content of your meals. It allows you to:

- Track food products and their nutritional values
- Create meals/plates by combining multiple foods
- Calculate total calories and nutrients based on portion sizes

## Features

- Food product database with nutritional information
- Meal composition tracking with customizable quantities
- Simple calorie and nutrient calculations
- Easy-to-use command line interface

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

## Example Usage

```python
# Create a meal
breakfast = Plate("Breakfast")
breakfast.add_product(apple, 1.5)  # 1.5 apples
breakfast.add_product(banana, 2)   # 2 bananas

# View nutrition info
print(f"Total calories: {breakfast.total_calories():.1f}kcal")
```
