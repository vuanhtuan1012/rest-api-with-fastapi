# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-10 18:55:32
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:09:11
"""
Database Interface
"""
from typing import Any, Dict

PostType = Dict[str, Any]
CommentType = Dict[str, Any]
POST_TABLE: Dict[int, PostType] = {}
COMMENT_TABLE: Dict[int, CommentType] = {}
