class ProductService:
    """Service class that handles product management operations using in-memory storage."""
    
    def __init__(self):
        """Initialize empty product storage and ID counter."""
        self.products = {}  # Dictionary to store products with ID as key
        self.counter = 1    # Auto-incrementing counter for product IDs

    def create_product(self, name, description, price):
        """
        Create a new product and store it in memory.
        
        Args:
            name (str): Product name
            description (str): Product description
            price (float): Product price
            
        Returns:
            dict: Created product with generated ID
        """
        product = {
            "id": self.counter,
            "name": name,
            "description": description,
            "price": price
        }
        self.products[self.counter] = product
        self.counter += 1
        return product

    def get_products(self):
        """
        Retrieve all products.
        
        Returns:
            list: List of all product dictionaries
        """
        return list(self.products.values())

    def update_product(self, product_id, name=None, description=None, price=None):
        """
        Update an existing product's attributes.
        
        Args:
            product_id (int): ID of product to update
            name (str, optional): New product name
            description (str, optional): New product description
            price (float, optional): New product price
            
        Returns:
            dict: Updated product or None if product not found
        """
        product = self.products.get(product_id)
        if not product:
            return None
        if name is not None:
            product["name"] = name
        if description is not None:
            product["description"] = description
        if price is not None:
            product["price"] = price
        return product

    def delete_product(self, product_id):
        """
        Delete a product by its ID.
        
        Args:
            product_id (int): ID of product to delete
            
        Returns:
            dict: Deleted product or None if product not found
        """
        return self.products.pop(product_id, None)