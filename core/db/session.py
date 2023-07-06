from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

Base = declarative_base()

# # 同步版本的数据库会话
# engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = SessionLocal()
#     print("db created", id(db))
#     try:
#         yield db
#     finally:
#         db.close()
#         print("db closed: ", id(db))



# # 异步版本的数据库会话
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, future=True, echo=True)

# 创建异步 SQLAlchemy 会话类
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# 异步 SQLAlchemy 会话依赖项
async def get_db():
    async with async_session() as session:
        yield session

