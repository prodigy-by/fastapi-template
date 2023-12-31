import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text
from schemas.posts import PostSchema
from core.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    slug = Column(String, unique=True, nullable=False)
    title = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.datetime.now)

    def to_read_model(self) -> PostSchema:
        return PostSchema(
            id=self.id,
            slug=self.slug,
            title=self.title,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
