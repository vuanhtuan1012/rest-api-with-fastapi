# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 18:51:38
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:00:49
"""
Comment models
"""
from pydantic import BaseModel


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
