import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop
import tornado.web
from models.database import init_db
from config import Config, port
from routes import merchant_routes

class MainApplication(tornado.web.Application):
    def __init__(self):
        settings = dict(debug=True)
        super().__init__(merchant_routes.routes, **settings)

async def main():
    await init_db()
    app = MainApplication()
    app.listen(port)
    print(f"Server listening on port {port}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    AsyncIOMainLoop().install()
    asyncio.run(main())
