
from fastapi import FastAPI
from routers import products, users, cart, orders

app = FastAPI(title="E-commerce App")

# Include routers for different functionalities
app.include_router(products.router)
app.include_router(users.router)
app.include_router(cart.router)
app.include_router(orders.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the E-commerce APP!"}
