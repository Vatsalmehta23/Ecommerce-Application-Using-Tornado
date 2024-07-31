import json
import bcrypt
from tornado.web import RequestHandler
from models.database import SessionLocal
from models.merchant import Merchant

class UserCreationHandler(RequestHandler):
    async def post(self):
        data = json.loads(self.request.body)
        name = data.get("name")
        mobileno = data.get("mobileno")
        password = data.get("password")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        async with SessionLocal() as session:
            async with session.begin():
                merchant = Merchant(name=name, mobileno=mobileno, password=hashed_password)
                session.add(merchant)
                await session.commit()
                self.write({"message": "User created successfully", "user_id": merchant.id})
