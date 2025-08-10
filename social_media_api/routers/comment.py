# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 19:00:29
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:09:18
"""
Comment routers
"""
from fastapi import APIRouter, HTTPException
from social_media_api.models.comment import Comment, CommentIn
from social_media_api.database import COMMENT_TABLE
from social_media_api.routers.post import get_post


router = APIRouter()


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
