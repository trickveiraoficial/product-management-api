import pytest
from app.services.product_service import ProductService

class TestProductService:
    @pytest.fixture
    def service(self):
        """Create a fresh ProductService instance for each test"""
        return ProductService()

    def test_create_product(self, service):
        """Test creating a new product"""
        product = service.create_product(
            name="Test Product",
            description="Test Description",
            price=99.99
        )
        
        assert product["id"] == 1
        assert product["name"] == "Test Product"
        assert product["description"] == "Test Description"
        assert product["price"] == 99.99

    def test_get_products(self, service):
        """Test retrieving all products"""
        # Create two test products
        product1 = service.create_product("Product 1", "Desc 1", 10.00)
        product2 = service.create_product("Product 2", "Desc 2", 20.00)
        
        products = service.get_products()
        
        assert len(products) == 2
        assert product1 in products
        assert product2 in products

    def test_update_product(self, service):
        """Test updating an existing product"""
        # Create initial product
        product = service.create_product("Old Name", "Old Desc", 10.00)
        
        # Update product
        updated = service.update_product(
            product_id=1,
            name="New Name",
            description="New Desc",
            price=20.00
        )
        
        assert updated["name"] == "New Name"
        assert updated["description"] == "New Desc"
        assert updated["price"] == 20.00
        assert updated["id"] == 1

    def test_update_product_not_found(self, service):
        """Test updating a non-existent product"""
        result = service.update_product(999, name="New Name")
        assert result is None

    def test_delete_product(self, service):
        """Test deleting a product"""
        # Create product
        product = service.create_product("Test", "Desc", 10.00)
        
        # Delete product
        deleted = service.delete_product(1)
        
        assert deleted == product
        assert len(service.get_products()) == 0

    def test_delete_product_not_found(self, service):
        """Test deleting a non-existent product"""
        result = service.delete_product(999)
        assert result is None