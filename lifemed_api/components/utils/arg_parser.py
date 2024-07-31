import argparse


class ArgParse:
    @staticmethod
    def set_parser():
        """Initiate the argument parser for the application

        Returns
        -------
        Named Tuple
            The application arguments
        """
        arg_parser = argparse.ArgumentParser(
            description="Run LifemedAPI report generator"
        )

        # Execute parse_args()
        return arg_parser.parse_args()
