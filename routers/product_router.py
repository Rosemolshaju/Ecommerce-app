from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Product
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_product(name: str, description: str, price: float, db: Session = Depends(get_db)):
    product = Product(name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
