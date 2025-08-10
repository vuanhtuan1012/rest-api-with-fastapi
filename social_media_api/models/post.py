# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:36:50
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:09:48
"""
Post models
"""
from pydantic import BaseModel
from social_media_api.models.comment import Comment


class PostIn(BaseModel):
    """
    Stores a post provided by the user
    """

    body: str


class Post(PostIn):
    """
    Stores a post sent to the database
    """

    id: int


class PostWithComments(BaseModel):
    """
    Stores a post with comments
    """

    post: Post
    comments: list[Comment]
