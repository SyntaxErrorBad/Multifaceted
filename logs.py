import logging
import os
from dotenv import load_dotenv

load_dotenv('data/.env')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('data/logs.log', encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
if os.getenv('LOGGING_FILE') == "True":
    logger.addHandler(file_handler)
