import logging
from logging import config

from lifemed_api.components.api.api import run_api
from lifemed_api.components.config import LOGGING_CONFIG

config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()


class LifemedAPI:
    @staticmethod
    def run(args=None):
        """
        Main function: manage the Lifemed API.
        """
        logger.info("Loading project lifemed_api...")

        run_api()

        logger.info("Ended process")
