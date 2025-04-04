from fastapi import FastAPI
from routers import product_router, cart_router, auth_router, order_router
from database import Base, engine

# Initialize the app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(product_router.router, prefix="/products", tags=["Products"])
app.include_router(cart_router.router, prefix="/cart", tags=["Cart"])
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
app.include_router(order_router.router, prefix="/orders", tags=["Orders"])
