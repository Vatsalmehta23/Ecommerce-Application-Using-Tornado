import json
import bcrypt
from tornado.web import RequestHandler
from sqlalchemy.future import select
from models.database import SessionLocal
from models.merchant import Merchant
from utils.token_utils import create_access_token

class AuthHandler(RequestHandler):
    async def post(self):
        data = json.loads(self.request.body)
        mobileno = data.get("mobileno")
        password = data.get("password")
        
        async with SessionLocal() as session:
            async with session.begin():
                result = await session.execute(
                    select(Merchant).where(Merchant.mobileno == mobileno)
                )
                merchant = result.scalar_one_or_none()
                
                if merchant and bcrypt.checkpw(password.encode('utf-8'), merchant.password.encode('utf-8')):
                    token = create_access_token({"sub": merchant.id})
                    self.write({"access_token": token})
                else:
                    self.set_status(401)
                    self.write({"error": "Invalid credentials"})
