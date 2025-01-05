import os
import logging
from pathlib import Path


list_of_files = [
    "QAWITHPDF/__init__.py",
    "QAWITHPDF/data_ingestion.py",
    "QAWITHPDF/embedding.py",
    "QAWITHPDF/model_api.py",
    "Experiments/experiments.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py",
]

for filepaht in list_of_files:
    filepath = Path(filepaht)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
