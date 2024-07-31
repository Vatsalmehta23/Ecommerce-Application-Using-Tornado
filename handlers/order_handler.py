import json
import datetime
from tornado.web import RequestHandler
from sqlalchemy.future import select
from models.database import SessionLocal
from models.razorpay_credential import RazorpayCredential
from models.merchant import Merchant
from models.order import Order
from utils.token_utils import verify_token
from utils.razorpay_utils import create_razorpay_order

class OrderHandler(RequestHandler):
    async def post(self):
        auth_header = self.request.headers.get("Authorization")
        if not auth_header:
            self.set_status(401)
            self.write({"error": "Missing authorization header"})
            return

        token = auth_header.split(" ")[1]
        payload = verify_token(token)
        if not payload:
            self.set_status(401)
            self.write({"error": "Invalid or expired token"})
            return
        
        data = json.loads(self.request.body)
        total_amount = data.get("total_amount")
        order_date_str = data.get("order_date", datetime.datetime.utcnow().isoformat())

        try:
            order_date = datetime.datetime.fromisoformat(order_date_str.replace('Z', ''))
        except ValueError:
            self.set_status(400)
            self.write({"error": "Invalid date format"})
            return

        async with SessionLocal() as session:
            async with session.begin():
                result = await session.execute(
                    select(Merchant).where(Merchant.id == payload["sub"])
                )
                merchant = result.scalar_one_or_none()

                if not merchant:
                    self.set_status(404)
                    self.write({"error": "Merchant not found"})
                    return

                razorpay_result = await session.execute(
                    select(RazorpayCredential).where(RazorpayCredential.merchant_id == merchant.id)
                )
                razorpay_credential = razorpay_result.scalar_one_or_none()

                if not razorpay_credential:
                    self.set_status(404)
                    self.write({"error": "Razorpay credentials not found"})
                    return

                try:
                    razorpay_order, elapsed_time = await create_razorpay_order(
                        amount=total_amount,
                        access_key=razorpay_credential.access_key,
                        access_secret=razorpay_credential.access_secret
                    )
                    print(f"Time taken to create Razorpay order: {elapsed_time:.4f} seconds")
                except Exception as e:
                    self.set_status(500)
                    self.write({"error": f"Failed to create Razorpay order: {str(e)}"})
                    return

                order = Order(
                    merchant_id=merchant.id,
                    total_amount=total_amount,
                    order_date=order_date,
                    razorpay_order_id=razorpay_order['id'] 
                )
                session.add(order)
                await session.commit()
                self.write({"order_id": order.id, "razorpay_order_id": razorpay_order['id']})
