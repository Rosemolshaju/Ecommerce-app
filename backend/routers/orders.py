from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Order, Product
from database import get_db

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def create_order(user_id: int, items: list, db: Session = Depends(get_db)):
    order_total = 0
    for item in items:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with id {item['product_id']} not found.")
        order_total += item["quantity"] * product.price

    order = Order(user_id=user_id, total_price=order_total, status="Pending")
    db.add(order)
    db.commit()
    db.refresh(order)  # Refresh to get the current state of the order
    return {"message": "Order placed successfully", "order_id": order.id}

@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
