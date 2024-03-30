import logging
import os
import datetime 
from pathlib import Path

# Get the current module name for logger identification
logger_name = "logger"
logger = logging.getLogger(logger_name)
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()

# Create a file handler with timestamped filename
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
log_file_name = Path("./logs") / f"{current_time}.log"
file_handler = logging.FileHandler(log_file_name)

# Define a common formatter for both handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
logger.info("Starting logger...")