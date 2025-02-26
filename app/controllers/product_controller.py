from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import CreateProduct, UpdateProduct 
from app.services.product_service import ProductService

# Create router instance for product endpoints
router = APIRouter()
# Initialize service layer for product operations
product_service = ProductService()

class ProductController:
    """Controller class that handles HTTP requests for product operations."""

    @router.post("/products", response_model=dict)
    def create_product(self, product: CreateProduct):
        """
        Create a new product using data from the request body.

        Args:
            product (CreateProduct): Validated product data from request

        Returns:
            dict: Created product data
        """
        return product_service.add_product(product)

    @router.get("/products", response_model=list)
    def get_products(self):
        """
        Retrieve all products.

        Returns:
            list: List of all product dictionaries
        """
        return product_service.get_all_products()

    @router.put("/products/{product_id}", response_model=dict)
    def update_product(self, product_id: int, product: UpdateProduct):
        """
        Update an existing product by ID.

        Args:
            product_id (int): ID of product to update
            product (UpdateProduct): Validated update data from request

        Returns:
            dict: Updated product data

        Raises:
            HTTPException: If product with given ID is not found
        """
        updated_product = product_service.update_product(product_id, product)
        if not updated_product:
            raise HTTPException(status_code=404, detail="Product not found")
        return updated_product

    @router.delete("/products/{product_id}", response_model=dict)
    def delete_product(self, product_id: int):
        """
        Delete a product by ID.

        Args:
            product_id (int): ID of product to delete

        Returns:
            dict: Success message

        Raises:
            HTTPException: If product with given ID is not found
        """
        success = product_service.delete_product(product_id)
        if not success:
            raise HTTPException(status_code=404, detail="Product not found")
        return {"message": "Product deleted successfully"}