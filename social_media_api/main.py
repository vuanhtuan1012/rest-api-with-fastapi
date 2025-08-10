# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-08 14:29:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 19:12:15
"""
Main application
"""
from fastapi import FastAPI
from social_media_api.routers.post import router as post_router
from social_media_api.routers.comment import router as comment_router

app = FastAPI()
app.include_router(post_router, tags=["post"])
app.include_router(comment_router, tags=["comment"])
