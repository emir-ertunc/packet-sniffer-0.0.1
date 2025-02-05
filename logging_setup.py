import logging
import os


LOG_FILE = "ids_combined_log.txt"


if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()


def setup_logger():
    logger = logging.getLogger("IDSLogger")
    logger.setLevel(logging.INFO)

   
    file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
