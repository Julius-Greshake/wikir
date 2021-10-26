"""Test cases for the wikir package."""
from wikir import __version__


def test_version() -> None:
    """It returns the correct version number."""
    assert __version__ == "0.1.0"
