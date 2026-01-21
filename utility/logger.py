import logging
from pathlib import Path

def setup_logger(log_file: Path) -> logging.Logger:
    logger = logging.getLogger("christmas_gifts")
    logger.setLevel(logging.INFO)

    # Skydd så att loggern inte får flera handlers
    if logger.handlers:
        return logger

    handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger