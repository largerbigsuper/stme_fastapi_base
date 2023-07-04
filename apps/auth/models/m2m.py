from sqlalchemy import Column, Table, Integer, ForeignKey, INT

from core.db.session import Base


relationship_user_role = Table(
    'relationship_user_role',
    Base.metadata,
    # Column("id", INT, primary_key=True, unique=True, comment='主键ID', index=True, autoincrement=True),
    Column("id", INT, primary_key=True, unique=True, comment='主键ID', index=True),
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True),
)

