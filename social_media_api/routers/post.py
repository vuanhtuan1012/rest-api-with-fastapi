# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:53:44
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 17:32:21
"""
Post routers
"""
from typing import Any, Dict, Optional
from fastapi import APIRouter, HTTPException
from social_media_api.models.post import (
    UserPost,
    UserPostIn,
    Comment,
    CommentIn,
    UserPostWithComments,
)

Post = Dict[str, Any]
CommentType = Dict[str, Any]
POST_TABLE: Dict[int, Post] = {}
COMMENT_TABLE: Dict[int, CommentType] = {}
router = APIRouter()


@router.post("/post", response_model=UserPost, status_code=201)
async def create_post(post: UserPostIn):
    """
    Creates a post
    """
    data = post.model_dump()
    new_id = max(POST_TABLE, default=0) + 1
    new_post = {**data, "id": new_id}
    POST_TABLE[new_id] = new_post
    return new_post


@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    """
    Returns a list of posts
    """
    return list(POST_TABLE.values())


def get_post(post_id: int) -> Optional[Post]:
    """
    Returns a post
    """
    return POST_TABLE.get(post_id)


@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    """
    Creates a post
    """
    post = get_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.model_dump()
    new_id = max(COMMENT_TABLE, default=0) + 1
    new_comment = {**data, "id": new_id}
    COMMENT_TABLE[new_id] = new_comment
    return new_comment


@router.get("/{post_id}/comment", response_model=list[Comment])
async def get_comments_on_post(post_id: int):
    """
    Returns a list of posts
    """
    return [comment for comment in COMMENT_TABLE.values() if comment["post_id"] == post_id]


@router.get("/post/{post_id}", response_model=UserPostWithComments)
async def get_post_with_comments(post_id: int):
    """
    Returns post with comments
    """
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = await get_comments_on_post(post_id)
    return {"post": post, "comments": comments}
