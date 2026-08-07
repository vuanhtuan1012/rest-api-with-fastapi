# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-08 14:29:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-07 10:33:43
"""
Main application
"""

from fastapi import FastAPI

from social_media_api.routers.comments import router as comment_router
from social_media_api.routers.posts import router as post_router

app = FastAPI(
    title="Social Media APIs",
    description="REST API for managing posts, comments and users",
    version="1.0.0",
)
app.include_router(post_router)
app.include_router(comment_router)
