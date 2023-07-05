from sqlalchemy.orm import Session

from apps.auth import curd, schemas
from core.config import settings

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

from core.db.session import Base
from core.db.session import engine


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # init roles
    role_list = []
    role_names = ["admin", "staff", "worker"]
    for name in role_names:
        role = curd.role.get_by_name(db, name)
        if role:
            role_list.append(role)
            continue
        role_create = schemas.RoleCreate(name=name, avatar="https://pic50.photophoto.cn/20190115/0017029538033826_b.jpg")
        role = curd.role.create(db, role_create)
        role_list.append(role)

    # init user
    user = curd.user.get_by_username(db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            is_active=True,
        )
        user = curd.user.create(db, obj_in=user_in)  # noqa: F841
        user.roles = [role_list[0]]
        db.add(user)
        db.commit()