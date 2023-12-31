from typing import List
from core.repository import AbstractRepository
from schemas.posts import PostSchema, PostSchemaAdd


class PostsService:
    def __init__(self, posts_repo: AbstractRepository):
        self.posts_repo: AbstractRepository = posts_repo()

    async def add_post(self, post: PostSchemaAdd) -> int:
        post_dict = post.dict()
        post_id = await self.posts_repo.add_one(post_dict)
        return post_id

    async def get_posts(self) -> List[PostSchema]:
        posts = await self.posts_repo.find_all()
        return posts
    
    async def get_post(self, id) -> PostSchema:
        post = await self.posts_repo.find_one_by_id(id)
        return post
