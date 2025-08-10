# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-08 14:29:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2025-08-10 11:22:33
"""
Main application
"""
from fastapi import FastAPI
from social_media_api.routers.post import router as post_router

app = FastAPI()
app.include_router(post_router, tags=["post"])
