# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-09 07:27:35
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-09 07:34:40
"""
Provides shared fixtures for routers tests
"""

import pytest
from httpx import AsyncClient


@pytest.fixture(name="endpoints")
def endpoints_fixture() -> dict[str, str]:
    """
    Provides endpoints
    """
    return {"posts": "/posts", "comments": "/comments"}


@pytest.fixture(name="sample_post")
async def post_fixture(async_client: AsyncClient, endpoints: dict[str, str]):
    """
    Provides a persisted post instance for tests that require an existing post in the database
    """
    response = await async_client.post(endpoints["posts"], json={"body": "Sample Post"})
    return response.json()


@pytest.fixture
async def sample_comment(async_client: AsyncClient, endpoints: dict[str, str], sample_post: dict):
    """
    Provides a persisted comment instance for tests that require an existing comment in the database
    """
    response = await async_client.post(
        endpoints["comments"],
        json={"body": "Sample Comment", "post_id": sample_post["id"]},
    )
    return response.json()
