from fastapi import APIRouter
from app.controllers.product_controller import ProductController

# Create a new APIRouter instance for product endpoints
router = APIRouter()
# Initialize the product controller that will handle business logic
controller = ProductController()

@router.post("/products", response_model=dict)
def create_product(product: dict):
    """
    Create a new product.
    
    Args:
        product (dict): Product data matching CreateProduct schema
        
    Returns:
        dict: Created product data
    """
    return controller.create_product(product)

@router.get("/products", response_model=list)
def get_products():
    """
    Get all products.
    
    Returns:
        list: List of all product dictionaries
    """
    return controller.get_products()

@router.put("/products/{product_id}", response_model=dict)
def update_product(product_id: int, product: dict):
    """
    Update an existing product.
    
    Args:
        product_id (int): ID of product to update
        product (dict): Updated product data matching UpdateProduct schema
        
    Returns:
        dict: Updated product data
    """
    return controller.update_product(product_id, product)

@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    """
    Delete a product.
    
    Args:
        product_id (int): ID of product to delete
        
    Returns:
        dict: Success message if product was deleted
    """
    return controller.delete_product(product_id)

def setup_routes(app):
    """
    Configure all product routes for the main FastAPI application.
    
    Args:
        app: FastAPI application instance
    """
    app.include_router(router)