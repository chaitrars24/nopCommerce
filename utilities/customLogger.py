import logging


class generateLogs:
    @staticmethod
    def logs():
        logging.basicConfig(filename=".\\Logs\\automation.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
