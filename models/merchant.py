from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base

class Merchant(Base):
    __tablename__ = 'merchant'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobileno = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    orders = relationship("Order", back_populates="merchant")
    razorpay_credentials = relationship("RazorpayCredential", back_populates="merchant")
