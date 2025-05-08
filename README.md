# MyPlateLens

MyPlateLens is a simple nutrition tracking application that helps you calculate the nutritional content of your meals.

## Installation

1. Install [uv](https://github.com/astral-sh/uv) (recommended Python package installer):
   ```bash
   pip install uv
   ```

2. Install MyPlateLens in development mode:
   ```bash
   uv pip install -e .
   ```

## Running the Application

After installation, you can run the application with:
```bash
python -m myplatelens
```

## Testing

To run tests (requires test dependencies):
```bash
uv pip install -e ".[test]"
pytest
```
