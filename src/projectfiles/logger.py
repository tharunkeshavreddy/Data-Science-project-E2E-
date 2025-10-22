import logging
import os
from datetime import datetime

Logfile=f"{datetime.now().strftime('%m_%d_%Y_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs",Logfile)

os.makedirs(log_path,exist_ok=True)

Logfilepath=os.path.join(log_path,Logfile)

logging.basicConfig(
    filename=Logfilepath,
    format="[%(asctime)s ] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
)




