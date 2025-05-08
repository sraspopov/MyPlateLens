from pathlib import Path
from typing import Optional
import tomllib
from loguru import logger

class Config:
    """Application configuration manager."""
    
    def __init__(self):
        self.data_path = Path("products.csv")
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from pyproject.toml."""
        try:
            with open("pyproject.toml", "rb") as f:
                config = tomllib.load(f)
                if "tool" in config and "myplatelens" in config["tool"]:
                    ml_config = config["tool"]["myplatelens"]
                    if "data_path" in ml_config:
                        self.data_path = Path(ml_config["data_path"])
        except FileNotFoundError:
            logger.warning("pyproject.toml not found, using default configuration")
