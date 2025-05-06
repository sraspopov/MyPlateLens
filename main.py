import sys
from loguru import logger
from models import Product, Plate
from database import ProductDatabase

def configure_logging() -> None:
    """Configure logging format and level."""
    logger.remove()  # Remove default handler
    logger.add(
        sys.stderr,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )

def main() -> None:
    """Main application entry point."""
    configure_logging()
    logger.info("Starting MyPlateLens application")
    
    try:
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
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
