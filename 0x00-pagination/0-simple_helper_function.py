#!/usr/bin/env python3
from typing import Tuple
""" module with one function index_range"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ compute the index start && end for page"""
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers")
    index_end: int = page * page_size
    index_start: int = index_end - page_size
    return (index_start, index_end)
