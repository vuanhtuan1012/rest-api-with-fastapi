# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-07 18:32:49
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-09 07:25:20
"""
Test fixtures
"""

import pytest


@pytest.fixture(name="user")
def user_fixture():
    """
    Fake user
    """
    print("\nfake user")
    return {"id": 1, "name": "Alice"}


# pylint:disable=W0613
def test_first_use_user_fixture(user):
    """
    First use the user fixture
    """


def test_second_use_user_fixture(user):
    """
    Second use the user fixture
    """


@pytest.fixture(scope="module", name="db")
def db_fixture():
    """
    Fake database connection
    """
    print("\nfake open database connection")
    yield
    print("\nfake close database connection")


def test_first_use_db_fixture(db):
    """
    First use the db fixture
    """


def test_second_use_db_fixture(db):
    """
    Second use the db fixture
    """


@pytest.fixture(autouse=True)
def setup_env():
    """
    Fake setup environment
    """
    print("\nfake setup environment")
