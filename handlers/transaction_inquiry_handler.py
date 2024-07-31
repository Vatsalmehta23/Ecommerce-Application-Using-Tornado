from tornado.web import RequestHandler
from sqlalchemy.future import select
from models.database import SessionLocal
from models import Order, RazorpayCredential
from utils.razorpay_utils import fetch_razorpay_order

class SimpleInquiryHandler(RequestHandler):
    async def get(self, order_id):
        try:
            order_id = int(order_id)
        except ValueError:
            self.set_status(400)
            self.write({"error": "Invalid order ID format"})
            return
        
        async with SessionLocal() as session:
            async with session.begin():
                result = await session.execute(
                    select(Order).where(Order.id == order_id)
                )
                order = result.scalar_one_or_none()
                
                if not order:
                    self.set_status(404)
                    self.write({"error": "Order not found"})
                    return
                
                credentials_result = await session.execute(
                    select(RazorpayCredential).where(RazorpayCredential.merchant_id == order.merchant_id)
                )
                razorpay_credential = credentials_result.scalar_one_or_none()
                
                if not razorpay_credential:
                    self.set_status(404)
                    self.write({"error": "Razorpay credentials not found"})
                    return
                
                try:
                    razorpay_order = await fetch_razorpay_order(
                        order.razorpay_order_id, 
                        razorpay_credential.access_key, 
                        razorpay_credential.access_secret
                    )
                except RuntimeError as e:
                    self.set_status(500)
                    self.write({"error": str(e)})
                    return
                
                self.write({
                    "razorpay_order_details": razorpay_order
                })

