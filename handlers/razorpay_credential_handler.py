import json
from tornado.web import RequestHandler
from sqlalchemy.future import select
from models.database import SessionLocal
from models.razorpay_credential import RazorpayCredential
from models.merchant import Merchant
from utils.token_utils import verify_token

class RazorpayCredentialHandler(RequestHandler):
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
        mobileno = data.get("mobileno")
        access_key = data.get("access_key")
        access_secret = data.get("access_secret")

        async with SessionLocal() as session:
            async with session.begin():
                result = await session.execute(
                    select(Merchant).where(Merchant.mobileno == mobileno)
                )
                merchant = result.scalar_one_or_none()

                if not merchant:
                    self.set_status(404)
                    self.write({"error": "User not found"})
                    return
                
                razorpay_credential = RazorpayCredential(
                    merchant_id=merchant.id,
                    access_key=access_key,
                    access_secret=access_secret
                )
                session.add(razorpay_credential)
                await session.commit()
                self.write({"razorpay_credential_id": razorpay_credential.id})
