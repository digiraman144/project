import logging
import os
from datetime import datetime

# Logs ke liye folder banado agar nahi hai
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# File name with date-time (unique har run ke liye)
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logging configuration with line number and logger name
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s [%(name)s] (%(filename)s:%(lineno)d) - %(message)s",
    level=logging.INFO
)

# Logger object
logger = logging.getLogger("ml_project_logger")

# Example usage (testing ke liye)
if __name__ == "__main__":
    logger.info("Logging system is working fine!")
    logger.warning("This is a warning!")
    logger.error("This is an error!")
