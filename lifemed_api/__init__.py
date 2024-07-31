from importlib.metadata import PackageNotFoundError, version  # type: ignore

from lifemed_api.app import LifemedAPI  # noqa # pylint: disable=unused-import

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
