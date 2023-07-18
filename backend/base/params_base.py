from typing import Generic, List, Optional, TypeVar
from fastapi import Query
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql import operators
from sqlalchemy import and_, func
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

ModelType = TypeVar("ModelType", bound=Base)


class QueryParamsBase:

    COMMON_SQL_OPERATORS = [
        "in", "icontains"
    ]

    def __init__(self) -> None:
        pass

    def get_setted_properties(self, ) -> List[str]:
        properties = []
        for name, value in vars(self).items():
            if value is not None:
                properties.append(name)
        return properties
    
    def _get_and_filters(self, model: Generic[ModelType]):
        # Initialize query filter
        query_filter = []
        # Get the attributes of ReportQueryParams class
        params_attributes = vars(self).keys()
        # Add dynamic filters based on query parameters
        for attr in params_attributes:
            value = getattr(self, attr)
            if value:
                column = getattr(model, attr.split("__")[0])
                if isinstance(column, InstrumentedAttribute):
                    if attr.endswith("__icontains"):
                        attr = attr.split("__")[0]  # Get the field name without the suffix
                        query_filter.append(func.lower(getattr(model, attr)).ilike(f"%{value.lower()}%"))
                    else:
                        query_filter.append(getattr(model, attr) == value)
        return and_(*query_filter)
    