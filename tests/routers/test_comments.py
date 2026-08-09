# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-09 07:51:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-09 08:00:07
"""
Performs tests on comments endpoint
"""

import pytest
from httpx import AsyncClient


@pytest.mark.usefixtures("db")
async def test_create_comment_success(
    async_client: AsyncClient, endpoints: dict, sample_post: dict
):
    """
    Ensures create-comment endpoint produces a new comment successfully
    """
    body = "Sample Comment"
    expected = {"id": 1, "body": body, "post_id": sample_post["id"]}

    response = await async_client.post(
        endpoints["comments"], json={"body": body, "post_id": sample_post["id"]}
    )
    assert response.status_code == 201
    assert expected.items() <= response.json().items()


@pytest.mark.usefixtures("db")
async def test_create_comment_failure(async_client: AsyncClient, endpoints: dict):
    """
    Ensures create-comment endpoint rejects invalid input and does not create new comment
    """
    response = await async_client.post(endpoints["comments"], json={"body": "Sample Comment"})
    assert response.status_code == 422
