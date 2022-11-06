"""
    This module tests web_scrape functions
"""
from src.web_scrape import main
from src.web_scrape import set_options


def test_len_of_set_options():
    assert len(set_options()) == 2


def test_parsed_items():
    result = main()
    assert "title" in result[0]
