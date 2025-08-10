# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:53:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:10:34
"""
Post routers
"""
from typing import Any, Dict, Optional
from fastapi import APIRouter, HTTPException
from social_media_api.models.post import Post, PostIn, PostWithComments
from social_media_api.models.comment import Comment
from social_media_api.database import POST_TABLE, COMMENT_TABLE, PostType, CommentType


router = APIRouter()


@router.post("/post", response_model=Post, status_code=201)
async def create_post(post: PostIn) -> PostType:
    """
    Creates a post
    """
    data = post.model_dump()
    new_id = max(POST_TABLE, default=0) + 1
    new_post = {**data, "id": new_id}
    POST_TABLE[new_id] = new_post
    return new_post


@router.get("/post", response_model=list[Post])
async def get_all_posts() -> list[PostType]:
    """
    Returns a list of posts
    """
    return list(POST_TABLE.values())


def get_post(post_id: int) -> Optional[PostType]:
    """
    Returns a post
    """
    return POST_TABLE.get(post_id)


@router.get("/post/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_post(post_id: int) -> list[CommentType]:
    """
    Returns a list of posts
    """
    return [comment for comment in COMMENT_TABLE.values() if comment["post_id"] == post_id]


@router.get("/post/{post_id}", response_model=PostWithComments)
async def get_post_with_comments(post_id: int) -> Dict[str, Any]:
    """
    Returns post with comments
    """
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = await get_comments_on_post(post_id)
    return {"post": post, "comments": comments}
