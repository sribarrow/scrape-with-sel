"""
    Unit test case for main module
"""
from python_template_repo.main import main


def test_main_called() -> None:
    year = main()
    assert year == 2022
