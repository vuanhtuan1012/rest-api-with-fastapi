# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-06 18:29:25
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-09 15:58:10
"""
Provides global fixtures
"""

from typing import AsyncGenerator, Generator

import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from social_media_api.database import COMMENT_TABLE, POST_TABLE
from social_media_api.main import app


@pytest.fixture(name="client")
def client_fixture() -> Generator:
    """
    Provides HTTP client
    """
    yield TestClient(app)


@pytest.fixture(name="async_client")
async def async_client_fixture(client) -> AsyncGenerator:
    """
    Provides async client
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=client.base_url) as async_client:
        yield async_client


@pytest.fixture
async def db() -> AsyncGenerator:
    """
    Provides database session
    """
    COMMENT_TABLE.clear()
    POST_TABLE.clear()
    yield
