"""
    Unit test case for main module
"""
from src.example import main


def test_main_year() -> None:
    year = main().year
    assert year == 2022


def test_main_month() -> None:
    month = main().month
    assert month == 11
