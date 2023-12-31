import datetime
from typing import Optional
from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    slug: str
    title: str
    content: str
    created_at: str
    updated_at: Optional[datetime.datetime]


class PostSchemaAdd(BaseModel):
    slug: str
    title: str
    content: str
