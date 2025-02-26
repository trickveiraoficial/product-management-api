# Unit Test Documentation for ProductService

This documentation describes the unit tests implemented for the `ProductService` class in the `app.services.product_service` module. The tests are written using the pytest framework and cover the main operations of the product service, including product creation, retrieval, update, and deletion.

## Fixture: service

**Objective:** Provide a fresh instance of `ProductService` for each test.

**Description:** This fixture is used in all tests to ensure that each test starts with a clean instance of `ProductService`, avoiding interference between tests.

**Implementation:** Returns a new instance of `ProductService` for each test that uses it.

## Test: test_create_product

**Objective:** Verify if a new product can be created correctly.

**Description:** This test creates a new product using the `create_product` method of `ProductService` and checks if the product is created with the correct attributes.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Call the `create_product` method with the parameters: `name="Test Product"`, `description="Test Description"`, `price=99.99`.
3. Verify if the returned product has an ID equal to 1.
4. Verify if the product's name, description, and price are correct.

**Expected Result:** The product is successfully created, and its attributes match the provided values.

## Test: test_get_products

**Objective:** Verify if all products can be retrieved correctly.

**Description:** This test creates two products and checks if the `get_products` method returns both products.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Create two products using `create_product`:
   - First product: `name="Product 1"`, `description="Desc 1"`, `price=10.00`.
   - Second product: `name="Product 2"`, `description="Desc 2"`, `price=20.00`.
3. Call the `get_products` method.
4. Verify if the returned list contains two products.
5. Verify if both created products are in the list.

**Expected Result:** The product list contains the two created products.

## Test: test_update_product

**Objective:** Verify if an existing product can be updated correctly.

**Description:** This test creates a product, updates its attributes using the `update_product` method, and checks if the updates were applied correctly.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Create a product with initial attributes: `name="Old Name"`, `description="Old Desc"`, `price=10.00`.
3. Call the `update_product` method with new values: `product_id=1`, `name="New Name"`, `description="New Desc"`, `price=20.00`.
4. Verify if the updated product has the new values for name, description, and price.
5. Verify if the product ID remains the same (1).

**Expected Result:** The product is successfully updated, and its attributes reflect the new values.

## Test: test_update_product_not_found

**Objective:** Verify the behavior when trying to update a non-existent product.

**Description:** This test attempts to update a product with a non-existent ID and checks if the method returns `None`.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Call the `update_product` method with a non-existent ID (999) and `name="New Name"`.
3. Verify if the result is `None`.

**Expected Result:** The method returns `None`, indicating that the product was not found.

## Test: test_delete_product

**Objective:** Verify if a product can be deleted correctly.

**Description:** This test creates a product, deletes it using the `delete_product` method, and checks if the product was removed from the product list.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Create a product: `name="Test"`, `description="Desc"`, `price=10.00`.
3. Call the `delete_product` method with the product's ID (1).
4. Verify if the product returned by the delete method is the same as the one created.
5. Verify if the product list is empty after deletion (using `get_products`).

**Expected Result:** The product is successfully deleted and is no longer present in the product list.

## Test: test_delete_product_not_found

**Objective:** Verify the behavior when trying to delete a non-existent product.

**Description:** This test attempts to delete a product with a non-existent ID and checks if the method returns `None`.

**Steps:**
1. Create an instance of `ProductService` using the `service` fixture.
2. Call the `delete_product` method with a non-existent ID (999).
3. Verify if the result is `None`.

**Expected Result:** The method returns `None`, indicating that the product was not found.

## Summary

The unit tests for `ProductService` cover the following functionalities:

- Creation of a new product.
- Retrieval of all products.
- Update of an existing product.
- Attempt to update a non-existent product.
- Deletion of an existing product.
- Attempt to delete a non-existent product.

All tests use the `service` fixture to ensure that each test is executed with a fresh instance of the service, ensuring independence and reliability of results.