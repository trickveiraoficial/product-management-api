This is a REST API built with FastAPI for managing products. The application follows a layered architecture pattern with controllers, services, models, routes and schemas.

## Project Structure

```
app/
├── controllers/     # Handle HTTP requests and responses
├── models/         # Data models
├── routes/         # API route definitions
├── schemas/        # Request/Response data validation
└── services/       # Business logic
```

## Core Components

### Models

`Product` - Represents a product entity with:
- id: integer
- name: string
- description: string
- price: float

### Schemas

`product_schema.py` defines two Pydantic models:

- `CreateProduct`: Schema for product creation
- `UpdateProduct`: Schema for product updates

### Controllers 

`ProductController` handles HTTP operations:

```python
POST /products     # Create new product
GET /products      # List all products  
PUT /products/{id} # Update product
DELETE /products/{id} # Delete product
```

### Service Layer

`ProductService` implements business logic:

- `create_product()`: Creates new product
- `get_products()`: Retrieves all products
- `update_product()`: Updates existing product
- `delete_product()`: Removes a product

### Routes

`product_routes.py` defines API endpoints and connects them to controller methods.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /products | Create new product |
| GET | /products | Get all products |  
| PUT | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |

## Dependencies

The main dependencies are:
- FastAPI - Web framework
- Pydantic - Data validation
- Uvicorn - ASGI server

To install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

The application can be started using:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`