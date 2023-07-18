from typing import Generic, List, Optional, TypeVar
from fastapi import Query
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql import operators
from sqlalchemy import and_
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

ModelType = TypeVar("ModelType", bound=Base)


class QueryParamsBase:

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
        params_attributes = dir(self)
        model_attributes = [attr for attr in params_attributes if not attr.startswith("_") and not callable(getattr(self, attr))]
        # Add dynamic filters based on query parameters
        for attr in model_attributes:
            attr_value = getattr(self, attr)
            if attr_value:
                column = getattr(model, attr)
                if isinstance(column, InstrumentedAttribute):
                    query_filter.append(getattr(model, attr) == attr_value)
        return and_(*query_filter)