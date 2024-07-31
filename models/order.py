from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from models.database import Base

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey('merchant.id'), nullable=False)
    total_amount = Column(Numeric, nullable=False)
    order_date = Column(DateTime, nullable=True)
    razorpay_order_id = Column(String, nullable=True) 
    
    merchant = relationship("Merchant", back_populates="orders")
