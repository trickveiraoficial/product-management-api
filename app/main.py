# Import the FastAPI framework to create the web application
from fastapi import FastAPI
# Import setup_routes function from product_routes to configure API endpoints
from app.routes.product_routes import setup_routes

# Initialize the FastAPI application instance
app = FastAPI()

# Configure all product-related routes for the application
setup_routes(app)

# Only run the server if this file is executed directly (not imported)
if __name__ == "__main__":
    # Import uvicorn ASGI server
    import uvicorn
    # Start the server on all network interfaces (0.0.0.0) on port 8000
    # with auto-reload enabled for development
    uvicorn.run(app, host="0.0.0.0", port=8000)