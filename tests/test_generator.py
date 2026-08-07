# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-07 11:01:41
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-07 11:16:12
"""
Test yield
"""

from typing import Generator

import pytest


@pytest.fixture(name="db")
def fixture_db() -> Generator:
    """
    Yields database
    """
    print("\nSetup env: database, user, etc.")
    yield "db"
    print("\nTeardown: cleanup env")


def test_generator(db):
    """
    Tests workflow while using generator in fixture
    """
    print("Do stuffs")
    assert db == "db"
