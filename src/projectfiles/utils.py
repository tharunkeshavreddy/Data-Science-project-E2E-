import os
import sys
import pandas as pd
from src.projectfiles.logger import logging
from src.projectfiles.exception import CustomException
from dotenv import load_dotenv
import pymysql



load_dotenv()


host=os.getenv("host")
user=os.getenv("user")
pswd=os.getenv("password")
db=os.getenv("db")


def readsqldata():
    logging.info("---------------reading sql started-----------")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=pswd,
            db=db
        )
        
        logging.info("-----------------Completed connection-------------%s",mydb)
        df=pd.read_sql_query("select * from stud",mydb)
        print(df.head(5))
        print("=============================================================")
        print(df.info())
        
        return df
        
        
        
        
    except Exception as e:
        raise CustomException(e,sys) from None
    




















