"""
    This is the main module for the application
"""
from datetime import datetime


def main() -> None:
    today = datetime.today()
    return today.year


if __name__ == "__main__":
    main()
