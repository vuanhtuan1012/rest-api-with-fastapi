# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 10:36:50
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 17:01:19
"""
Post models
"""
from pydantic import BaseModel


class UserPostIn(BaseModel):
    """
    Stores a post provided by the user
    """

    body: str


class UserPost(UserPostIn):
    """
    Stores a post sent to the database
    """

    id: int


class CommentIn(BaseModel):
    """
    Stores a comment provided by the user
    """

    body: str
    post_id: int


class Comment(CommentIn):
    """
    Stores a comment sent to the database
    """

    id: int


class UserPostWithComments(BaseModel):
    """
    Stores a post with comments
    """

    post: UserPost
    comments: list[Comment]
