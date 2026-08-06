# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 19:00:29
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-06 09:37:58
"""
Comment endpoints
"""
from fastapi import APIRouter, HTTPException

from database import COMMENT_TABLE
from schemas.comment import Comment, CommentIn
from routers.posts import get_post

router = APIRouter(prefix="/comments", tags=["Comments"])


@router.post("", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    """
    Creates a comment
    """
    post = get_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    data = comment.model_dump()
    new_id = max(COMMENT_TABLE, default=0) + 1
    new_comment = {**data, "id": new_id}
    COMMENT_TABLE[new_id] = new_comment
    return new_comment
