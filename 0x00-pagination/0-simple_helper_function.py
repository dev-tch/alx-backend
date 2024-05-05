#!/usr/bin/env python3
from typing import Tuple
""" module with one function index_range"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ compute the index start && end for page"""
    index_start: int = (page - 1) * page_size
    index_end: int = page * page_size
    return (index_start, index_end)
