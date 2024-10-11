"""
Tests of mylib goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    extract_results = extract()
    assert extract_results is not None


def test_load():
    load_results = load()
    assert load_results is not None


def test_query():
    query_results = query()
    assert query_results is not None


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
