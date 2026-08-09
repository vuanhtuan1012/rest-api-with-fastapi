# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-08 18:24:40
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-09 08:12:10
"""
Performs tests on posts endpoints
"""

import pytest
from httpx import AsyncClient


@pytest.mark.usefixtures("db")
async def test_create_post_success(async_client: AsyncClient, endpoints: dict):
    """
    Ensures the create-post endpoint produces a new post successfully
    """
    body = "Sample Post"
    expected = {"id": 1, "body": body}

    response = await async_client.post(endpoints["posts"], json={"body": body})
    assert response.status_code == 201
    assert expected.items() <= response.json().items()


@pytest.mark.usefixtures("db")
async def test_create_post_failure(async_client: AsyncClient, endpoints: dict):
    """
    Ensures the create-post endpoint rejects invalid input and does not create a new post
    """
    response = await async_client.post(endpoints["posts"], json={})
    assert response.status_code == 422


@pytest.mark.usefixtures("db")
async def test_get_all_posts_empty_database(async_client: AsyncClient, endpoints: dict):
    """
    Ensures the get-all-posts endpoint returns an empty list when the database has no posts
    """
    response = await async_client.get(endpoints["posts"])
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.usefixtures("db")
async def test_get_all_posts_with_data(
    async_client: AsyncClient, endpoints: dict, sample_post: dict
):
    """
    Ensures the get-all-posts endpoint returns all existing posts when the database contains data
    """
    response = await async_client.get(endpoints["posts"])
    assert response.status_code == 200
    assert response.json() == [sample_post]


@pytest.mark.usefixtures("db")
async def test_get_post_success(async_client: AsyncClient, endpoints: dict, sample_post: dict):
    """
    Ensures the get-post endpoint retrieves the requested post successfully
    """
    post_id = sample_post["id"]
    expected = {"post": sample_post}
    response = await async_client.get(f"{endpoints['posts']}/{post_id}")
    assert response.status_code == 200
    assert expected.items() <= response.json().items()


@pytest.mark.usefixtures("db")
async def test_get_post_failure(async_client: AsyncClient, endpoints: dict):
    """
    Ensures the get-post endpoint returns an error when the requested post does not exist
    """
    respose = await async_client.get(f"{endpoints['posts']}/999")
    assert respose.status_code == 404


@pytest.mark.usefixtures("db")
async def test_get_comments_no_comments(
    async_client: AsyncClient, endpoints: dict, sample_post: dict
):
    """
    Ensures the get comments on post has no comments returns an empty list
    """
    response = await async_client.get(f"{endpoints['posts']}/{sample_post['id']}/comments")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.usefixtures("db")
async def test_get_comments_with_data(
    async_client: AsyncClient, endpoints: dict, sample_post: dict, sample_comment: dict
):
    """
    Ensures the get comments on post has existing comments returns all comments
    """
    response = await async_client.get(f"{endpoints['posts']}/{sample_post['id']}/comments")
    assert response.status_code == 200
    assert response.json() == [sample_comment]


@pytest.mark.usefixtures("db")
async def test_get_post_with_comments_success(
    async_client: AsyncClient, endpoints: dict, sample_post: dict, sample_comment: dict
):
    """
    Ensures the get-post-with-comments endpoints retrieves a post with all its comments
    """
    expected = {"post": sample_post, "comments": [sample_comment]}
    response = await async_client.get(f"{endpoints['posts']}/{sample_post['id']}")
    assert response.status_code == 200
    assert expected == response.json()


@pytest.mark.usefixtures("db")
async def test_get_post_with_comments_failure(async_client: AsyncClient, endpoints: dict):
    """
    Ensures the get-post-with-comments endpoints returns an error
    when the requested post does not exist
    """
    response = await async_client.get(f"{endpoints['posts']}/999")
    assert response.status_code == 404
