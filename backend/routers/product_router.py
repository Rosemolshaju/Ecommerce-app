from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Products
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_products(name: str, description: str, price: float, db: Session = Depends(get_db)):
    products = Products(name=name, description=description, price=price)
    db.add(products)
    db.commit()
    db.refresh(products)
    return products

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
