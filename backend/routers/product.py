
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Product
from database import get_db
router = APIRouter(prefix="/products", tags=["Products"])
@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
@router.post("/")
def create_product(name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price, stock=stock)
    db.add(product)
    db.commit()
    return {"message": "Product created successfully"}
@router.put("/{product_id}")
def update_product(product_id: int, name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product.name = name
    product.description = description
    product.price = price
    product.stock = stock
    db.commit()
    return {"message": "Product updated successfully"}
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
