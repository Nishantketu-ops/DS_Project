from src.simplemlProject.logger import logging
from src.simplemlProject.exception import CustomException
from src.simplemlProject.components.data_injestion import DataInjestion
from src.simplemlProject.components.data_injestion import DataInjestionConfig

import sys

if __name__=="__main__":
    logging.info("The execution has started.")

    try:
        # data_injestion_config=DataInjestionConfig()
        data_injestion= DataInjestion()
        data_injestion.initiate_data_injestion()
        

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)