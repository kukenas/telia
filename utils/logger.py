import logging
from logging.handlers import RotatingFileHandler


class Logger:
    FORMAT = "[%(asctime)s - %(name)s - %(levelname)s] : %(message)s"
    LOG_SIZE = 3 * 1024 * 1024

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path
        self.log = self.get_logger()

    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.ERROR)
        logger.addHandler(self.get_rotating_handler(self.path))
        logger.addHandler(self.get_console_handler())
        return logger

    @staticmethod
    def get_rotating_handler(path):
        # Rotating File Handler
        log_handler = RotatingFileHandler(path, mode='a',
                                          maxBytes=Logger.LOG_SIZE,
                                          backupCount=10)
        log_handler.setFormatter(logging.Formatter(Logger.FORMAT))
        log_handler.setLevel(logging.ERROR)
        return log_handler

    @staticmethod
    def get_console_handler():
        # Console Handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter(Logger.FORMAT))
        return ch

    @property
    def logger(self):
        return self.log


LOG = Logger("TeliaChallenge", "../logs/application.log").logger
