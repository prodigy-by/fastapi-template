from models import Post
from core.repository import SQLAlchemyRepository


class PostRepository(SQLAlchemyRepository):
    model = Post
