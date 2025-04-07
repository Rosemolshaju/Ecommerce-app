from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Cart
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_to_cart(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    cart_item = CartItem(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)
    return cart_item

@router.get("/")
def get_cart(user_id: int, db: Session = Depends(get_db)):
    return db.query(CartItem).filter(CartItem.user_id == user_id).all()
