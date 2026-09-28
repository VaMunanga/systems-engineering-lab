from sqlmodel import Field, SQLModel, create_engine, Session
from dotenv import load_dotenv 
import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()

class Hero(SQLModel,table=True):
    id:int | None = Field(default=None, primary_key=True)
    name:str
    secret_name:str
    age:int | None = None


database_url = os.getenv("DATABASE_URL")

engine = create_async_engine(database_url,echo=True)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

asyncio.run(create_db())


