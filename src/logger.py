import logging
import os
from datetime import datetime


log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

log_dir = os.path.join(os.getcwd(), "logs")


os.makedirs(log_dir, exist_ok=True)


log_file_path = os.path.join(log_dir, log_filename)


logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)


