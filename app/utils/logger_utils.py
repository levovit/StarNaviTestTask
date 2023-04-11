import os
import logging


def get_logger(module_name: str):
    log_file = os.path.join("logs", f"{module_name}.log")
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "{asctime} | {levelname: <8} | {name: <8} | {message}", style="{"
    )

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
