from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class RazorpayCredential(Base):
    __tablename__ = 'razorpay_credentials'
    
    id = Column(Integer, primary_key=True, index=True)
    merchant_id = Column(Integer, ForeignKey('merchant.id'), nullable=False)
    access_key = Column(String, nullable=False)
    access_secret = Column(String, nullable=False)
    
    merchant = relationship("Merchant", back_populates="razorpay_credentials")
