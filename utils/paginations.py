import math
from typing import Generic, List, TypeVar
from pydantic import Field

from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.sql.selectable import Select
from core.db.session import Base
from pydantic.generics import GenericModel


M = TypeVar('M')

class PageResponse(GenericModel, Generic[M]):
    limit: int = Field(description='max count returned of one page')
    page: int = Field(description='cunrrent page number')
    total: int = Field(description='total count of hits')
    pages: int = Field(description='total pages of hits')
    items: List[M] = Field(description='List of items returned in the response following given criteria')


class Page:
    def __init__(self, items, page, limit, total):
        self.items = items
        self.limit = limit
        self.page = page
        self.total = total
        self.pages = int(math.ceil(total / float(limit)))


def paginate(db: Session, query: Select, table: Base, page=1, limit=20):
    if page <= 0:
        raise AttributeError('page needs to be >= 1')
    if limit <= 0:
        raise AttributeError('page_size needs to be >= 1')
    items = db.execute(query.limit(limit).offset((page - 1) * limit)).scalars().all()
    # count
    count_query = query.with_only_columns(func.count(table.id))
    total = db.execute(count_query).scalar_one()
    return Page(items, page, limit, total).__dict__
