from repository.posts import PostRepository
from services.posts import PostsService


def posts_service() -> PostsService:
    return PostsService(PostRepository)
