import csv
import os
from pathlib import Path
import logging
import time



# def set_logger():
#     task_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
#     logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#     Path("log/").mkdir(parents=True, exist_ok=True)
#     fh = logging.FileHandler('log/{}.log'.format(task_time))
#     fh.setLevel(logging.DEBUG)
#     ch = logging.StreamHandler()
#     ch.setLevel(logging.WARN)
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     fh.setFormatter(formatter)
#     ch.setFormatter(formatter)
#     logger.addHandler(fh)
#     logger.addHandler(ch)
    
#     return logger

def set_logger():
    task_time = time.strftime("%Y-%m-%d_%H:%M", time.localtime())
    logging.basicConfig(level=logging.INFO,format ='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    log_dir = Path("log/")
    task_time = time.strftime("%Y-%m-%d_%H-%M", time.localtime())
    log_file_path = log_dir / '{}.log'.format(task_time)
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARN)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger
