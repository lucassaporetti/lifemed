import logging
from logging import config
from importlib.metadata import PackageNotFoundError, version  # type: ignore
import uvicorn
from fastapi import FastAPI

from lifemed_api.components.api.exception_handlers import include_exception_handlers
from lifemed_api.components.api.middleware import include_middleware
from lifemed_api.components.routes.routes import include_routers
from lifemed_api.components.config import LOGGING_CONFIG, envs


config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return "/healthz" not in record.getMessage()


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


def api_factory():
    try:
        __version__ = version(__name__)
    except PackageNotFoundError:  # pragma: no cover
        __version__ = "unknown"

    app = FastAPI(
        title="Lifemed API",
        description="",
        version=__version__,
        docs_url="/swagger",
        redoc_url="/docs",
    )

    include_middleware(app, logger)
    include_exception_handlers(app, logger)
    include_routers(app)

    logger.info("API load completed")

    return app


app = api_factory()


def run_api():
    uvicorn.run(app, host=envs.HOST_IP, port=envs.HOST_PORT, debug=True)


if __name__ == "__main__":
    run_api()
