class Product:
    """
    Model class representing a product entity.
    
    Attributes:
        id (int): Unique identifier for the product
        name (str): Name of the product
        description (str): Description of the product
        price (float): Price of the product
    """

    def __init__(self, id: int, name: str, description: str, price: float):
        """
        Initialize a new Product instance.

        Args:
            id (int): Unique identifier for the product
            name (str): Name of the product
            description (str): Description of the product
            price (float): Price of the product
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        """
        Convert the product instance to a dictionary.

        Returns:
            dict: Product data in dictionary format
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price
        }