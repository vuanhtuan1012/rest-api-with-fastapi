# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:53:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-06 09:38:03
"""
Posts endpoints
"""
from typing import Any, Optional

from fastapi import APIRouter, HTTPException

from database import COMMENT_TABLE, POST_TABLE
from schemas.comment import Comment
from schemas.post import Post, PostIn, PostWithComments

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("", response_model=Post, status_code=201)
async def create_post(post: PostIn):
    """
    Creates a post
    """
    data = post.model_dump()
    new_id = max(POST_TABLE, default=0) + 1
    new_post = {**data, "id": new_id}
    POST_TABLE[new_id] = new_post
    return new_post


@router.get("", response_model=list[Post])
async def get_all_posts():
    """
    Returns a list of posts
    """
    return list(POST_TABLE.values())


def get_post(post_id: int) -> Optional[dict[str, Any]]:
    """
    Returns a post
    """
    return POST_TABLE.get(post_id)


@router.get("/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_post(post_id: int):
    """
    Returns a list of posts
    """
    return [comment for comment in COMMENT_TABLE.values() if comment["post_id"] == post_id]


@router.get("/{post_id}", response_model=PostWithComments)
async def get_post_with_comments(post_id: int):
    """
    Returns post with comments
    """
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = await get_comments_on_post(post_id)
    return {"post": post, "comments": comments}
