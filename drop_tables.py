# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from config import Config

# Base = declarative_base()
# engine = create_async_engine(Config.SqlAlchemy_Uri, echo=True)

# async def drop_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         print("All tables dropped.")

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(drop_tables())
