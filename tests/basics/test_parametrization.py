# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2026-08-08 02:02:25
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2026-08-08 02:18:32
"""
Test parameterization
"""

import pytest


@pytest.mark.parametrize("number", [2, 4, 6])
def test_is_even(number):
    """
    Checks whether number is even
    """
    assert number % 2 == 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-5, -3, -8),
        (10, -20, -10),
    ],
    ids=["positive numbers", "negative numbers", "mix numbers"],
)
def test_add(a, b, expected):
    """
    Performs addition tests
    """
    result = a + b
    assert result == expected
