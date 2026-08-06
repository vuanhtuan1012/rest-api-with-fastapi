# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2025-08-08 14:29:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-06 12:04:17
"""
Main application
"""
import uvicorn
from fastapi import FastAPI

from routers.comments import router as comment_router
from routers.posts import router as post_router

app = FastAPI(
    title="Social Media APIs",
    description="REST API for managing posts, comments and users",
    version="1.0.0",
)
app.include_router(post_router)
app.include_router(comment_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
