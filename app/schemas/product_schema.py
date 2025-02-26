from pydantic import BaseModel
from typing import Optional

class CreateProduct(BaseModel):
    """
    Pydantic model for validating product creation requests.

    Attributes:
        name (str): Required name of the product
        description (Optional[str]): Optional product description, defaults to None
        price (float): Required product price
    """
    name: str
    description: Optional[str] = None
    price: float

class UpdateProduct(BaseModel):
    """
    Pydantic model for validating product update requests.
    All fields are optional since updates may be partial.

    Attributes:
        name (Optional[str]): New product name, if provided
        description (Optional[str]): New product description, if provided
        price (Optional[float]): New product price, if provided
    """
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None