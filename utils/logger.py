import logging
import os

def get_logger(name="framework"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler("logs/test.log")
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
