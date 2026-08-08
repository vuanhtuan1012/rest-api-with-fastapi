# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-08 09:31:04
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-08 12:28:47
"""
Performs tests on posts API
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest
from httpx import HTTPStatusError

from tests.basics.async_posts import async_get_post
from tests.basics.posts import PostService, get_post


def test_get_post_from_database():
    """
    Checks that the database returns the expected post
    """
    repository = Mock()
    repository.get.return_value = {
        "userId": 1,
        "id": 1,
        "title": "fake title",
        "body": "fake body",
    }
    post_service = PostService(repository)
    result = post_service.get_post_by_id(1)
    expected = {"id": 1}
    assert expected.items() <= result.items()


def test_get_post_from_api():
    """
    Checks that the API returns the expected post
    """
    with patch("tests.basics.posts.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "userId": 1,
            "id": 1,
            "title": "fake title",
            "body": "fake body",
        }
        result = get_post(1)
    expected = {"id": 1}
    assert expected.items() <= result.items()


def test_get_post_db_error():
    """
    Checks that the database triggers the expected exception
    """
    repository = Mock()
    repository.get.side_effect = ConnectionError("Database unavailable")
    post_service = PostService(repository)
    with pytest.raises(ConnectionError):
        post_service.get_post_by_id(1)


async def test_async_get_post():
    """
    Checks that the async function returns the expected post
    """
    response = Mock()
    response.json.return_value = {
        "userId": 1,
        "id": 1,
        "title": "fake title",
        "body": "fake body",
    }

    client = AsyncMock()
    client.get.return_value = response

    result = await async_get_post(client, 1)
    expected = {"id": 1}
    assert expected.items() <= result.items()


async def test_async_get_post_http_error():
    """
    Checks that the async function triggers the expected exception
    """
    response = Mock()
    response.raise_for_status.side_effect = HTTPStatusError(
        "404 Not Found", request=Mock(), response=Mock()
    )

    client = AsyncMock()
    client.get.return_value = response

    with pytest.raises(HTTPStatusError):
        await async_get_post(client, 999)
