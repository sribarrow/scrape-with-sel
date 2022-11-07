"""
    This module tests web_scrape functions
"""
import sys
from unittest.mock import create_autospec

import pytest
from src.web_scrape import main
from src.web_scrape import set_options


@pytest.fixture
def mock_main():
    return {"title": "test title"}


@pytest.mark.set_options
def test_len_of_set_options():
    assert len(set_options()) == 2


@pytest.mark.xfail
def test_len_of_set_options_invalid():
    assert len(set_options()) == 1


# @pytest.mark.skip("needs mock")
def test_parsed_items():
    mock_function = create_autospec(main, return_value={"title": "test title"})
    expected = "test title"
    actual = mock_function()
    assert actual["title"] == expected


@pytest.mark.skipif(sys.version_info.major < 3, reason="requires minimum python 3.10")
def test_for_skipif():
    pass
