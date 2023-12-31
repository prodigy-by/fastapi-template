from fastapi import APIRouter, Depends
from schemas.posts import PostSchemaAdd
from services.posts import PostsService
from core.dependencies import posts_service

router = APIRouter(
    prefix="/posts",
)


@router.post("/")
async def add_post(
    post: PostSchemaAdd,
    posts_service: PostsService = Depends(posts_service),
):
    post_id = await posts_service.add_post(post)
    return {"post_id": post_id}


@router.get("/")
async def get_posts(
    posts_service: PostsService = Depends(posts_service),
):
    posts = await posts_service.get_posts()
    return posts

@router.get("/{post_id:int}")
async def get_post(
    post_id: int,
    posts_service: PostsService = Depends(posts_service)
):
    post = await posts_service.get_post(post_id)
    return post