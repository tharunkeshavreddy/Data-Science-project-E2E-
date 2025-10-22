import os
import sys
from src.projectfiles.exception import CustomException
from src.projectfiles.logger import logging
import pandas as pd
from src.projectfiles.utils import readsqldata
from sklearn.model_selection import train_test_split




from dataclasses import dataclass


@dataclass
class dataingestionconfig:
    traindatapath:str=os.path.join('artifact','train.csv')
    testdatapath:str=os.path.join('artifact','test.csv')
    rawdatapath:str=os.path.join('artifact','raw.csv')
    
    
    
class dataingestion:
    def __init__(self):
        self.ingestionconfig=dataingestionconfig()
        
        
    def initiatedataingestion(self):
        try:
            #reading data
            df=readsqldata()
            logging.info("-----------Read data from sql-------------------")
            
            os.makedirs(os.path.dirname(self.ingestionconfig.traindatapath),exist_ok=True)
            
            
            
            df.to_csv(self.ingestionconfig.rawdatapath,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=43)
            
            df.to_csv(self.ingestionconfig.traindatapath,index=False,header=True)
            df.to_csv(self.ingestionconfig.testdatapath,index=False,header=True)
            
            
            logging.info("-------------data ingestion is completed")
            
            
            return(
                self.ingestionconfig.traindatapath,
                self.ingestionconfig.testdatapath
            )
            
            
            
            
        except Exception as e:
            raise CustomException(e,sys) from None






