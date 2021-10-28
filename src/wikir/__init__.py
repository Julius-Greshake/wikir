"""Print a random wikipedia page to the console."""
try:
    from importlib.metadat import version, PackageNotFoundError  # type: ignore
except ImportError:  # pgrama: no cov er
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"