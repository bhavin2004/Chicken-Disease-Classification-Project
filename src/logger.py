import logging
import os
import sys
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d-%m-%Y->%H:%M:%S')}.log"

LOG_PATH = os.path.join(os.getcwd(),'logs',LOG_FILE)

os.makedirs(LOG_PATH,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    # filename=os.path.join(LOG_PATH,LOG_FILE),
    format='[%(asctime)s]: %(levelname)s : %(name)s : %(module)s at %(lineno)d => %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_PATH,LOG_FILE)),
        logging.StreamHandler(sys.stdout)
    ]
        
)




