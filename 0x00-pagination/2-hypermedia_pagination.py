#!/usr/bin/env python3
""" module with one function index_range and class Server"""
from typing import Tuple
import csv
import math
from typing import List
from typing import Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ compute the index start && end for page"""
    index_start: int = (page - 1) * page_size
    index_end: int = page * page_size
    return (index_start, index_end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return page from dataset """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index_start, index_end = index_range(page, page_size)
        mylist = self.dataset()
        if index_end <= len(mylist) and index_end <= len(mylist):
            return mylist[index_start: index_end]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia pagination"""
        data = self.get_page(page, page_size)
        size_dataset: int = len(self.__dataset)
        total_pages = math.ceil(size_dataset / page_size)
        start_index, end_index = index_range(page, page_size)
        return {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': (page + 1) if end_index < size_dataset else None,
                'prev_page': (page - 1) if start_index > 0 else None,
                'total_pages': total_pages
                }
