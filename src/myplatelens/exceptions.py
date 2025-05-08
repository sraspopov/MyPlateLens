class ProductNotFoundError(Exception):
    """Raised when a requested product is not found."""
    pass

class InvalidProductDataError(Exception):
    """Raised when product data fails validation."""
    pass

class DataSourceError(Exception):
    """Base class for data source related errors."""
    pass

class FileNotFoundError(DataSourceError):
    """Raised when data file is not found."""
    pass

class InvalidFormatError(DataSourceError):
    """Raised when data format is invalid."""
    pass
