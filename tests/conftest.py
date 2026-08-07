# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-06 18:29:25
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-07 15:06:30
"""
Configuration tests
"""

from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from social_media_api.database import COMMENT_TABLE, POST_TABLE
from social_media_api.main import app


@pytest.fixture(scope="session")
def anyio_backend() -> str:
    """
    Declares async runtime used
    """
    return "asyncio"


@pytest.fixture(name="client")
def http_client() -> Generator:
    """
    Provides HTTP client
    """
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    """
    Provides database session
    """
    COMMENT_TABLE.clear()
    POST_TABLE.clear()
    yield


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    """
    Provides async client
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=client.base_url) as async_cli:
        yield async_cli
