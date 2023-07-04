from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# 同步版本的数据库会话
engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    print("db created", id(db))
    try:
        yield db
    finally:
        db.close()
        print("db closed: ", id(db))



# # 异步版本的数据库会话
# async_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True, future=True)
# AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

# Base = declarative_base()

# def get_sync_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def get_async_db():
#     db = AsyncSessionLocal()
#     try:
#         yield db
#     finally:
#         await db.close()
