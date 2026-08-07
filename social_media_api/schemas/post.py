# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:36:50
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-07 09:38:47
"""
Post models
"""

from pydantic import BaseModel

from social_media_api.schemas.comment import Comment


class PostIn(BaseModel):
    """
    Represents the incoming post data sent to the API.
    Used for validating and storing fields provided by the client.
    """

    body: str


class Post(PostIn):
    """
    Represents the post data returned to the client.
    Used for formating and sending post information in API responses.
    """

    id: int


class PostWithComments(BaseModel):
    """
    Represents the post data, including its associated comments,
    returned to the client in API responses.
    """

    post: Post
    comments: list[Comment]
