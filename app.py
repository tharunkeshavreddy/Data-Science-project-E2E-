from src.projectfiles.logger import logging
from src.projectfiles.exception import CustomException
import sys
from src.projectfiles.components.data_injection import dataingestion,dataingestionconfig


if __name__=="__main__":
    logging.info(".................................The execution has started............................")
    
    
    
    try:
        data_injection_config=dataingestionconfig()
        data_ingestion=dataingestion()
        data_ingestion.initiatedataingestion()
    except Exception as e:
        logging.info("Exception")
        raise CustomException(e,sys) from None