from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth import curd, schemas
from apps.wes import models
from core.config import settings
from core.db.session import Base, engine

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28



async def init_db(db: AsyncSession) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    # await db.run_sync(Base.metadata.create_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # init roles
    role_list = []
    role_names = ["admin", "staff", "worker"]
    for name in role_names:
        role = await curd.role.get_by_name(db, name)
        if role:
            role_list.append(role)
            continue
        role_create = schemas.RoleCreate(name=name, avatar="https://pic50.photophoto.cn/20190115/0017029538033826_b.jpg")
        role = await curd.role.create(db, role_create)
        print(role)
        role_list.append(role)

    # init user
    user = await curd.user.get_by_username(db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            is_active=True,
            roles=[schemas.RoleInfo(id=1, name=role_names[0])]
        )
        user = await curd.user.create(db, obj_in=user_in)  # noqa: F841

