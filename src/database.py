from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mypy.names import DECLARATIVE_BASE

from src.config import settings

engine = create_async_engine(settings.DB_URL)

async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

#Base = declarative_base()

class Base(DeclarativeBase):
   pass