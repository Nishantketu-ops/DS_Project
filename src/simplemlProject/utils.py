import os
import sys
from src.simplemlProject.exception import CustomException
from src.simplemlProject.logger import logging
import pandas as pd 
from dotenv import load_dotenv
import pymysql
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')


def read_sql_data():
    logging.info("Reading sql database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password = password,
            db = db
        )

        logging.info("connection established!!!!",mydb)

        df=pd.read_sql_query('select * from students',mydb)
        print(df.head())

        return df 


    except Exception as ex :
        raise CustomException(ex)