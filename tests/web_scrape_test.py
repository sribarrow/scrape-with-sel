"""
    This module tests web_scrape functions
"""
from src.web_scrape import main


def test_failure():
    result = main()
    assert 1 == result
