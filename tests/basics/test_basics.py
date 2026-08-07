# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-06 17:02:30
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-07 17:48:37
"""
Basics of pytest
"""

import pytest


def test_add_two():
    """
    Performs a basic test case
    """
    x = 1
    y = 2
    assert x + y == 3


def test_dict_contains():
    """
    Check whether one dictionary is a subset of another.
    """
    actual = {"name": "Alice", "age": 23}
    expected = {"name": "Alice"}
    assert expected.items() <= actual.items()


def test_divide_by_zero():
    """
    Verifies that the expected error is raised.
    """
    # verify the error type
    with pytest.raises(ZeroDivisionError) as exc_info:
        assert 10 / 0

    # verify the error message
    assert str(exc_info.value) == "division by zero"
