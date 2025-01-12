import sys
from src.chicken_disease_classifier.config.configuration import ConfigurationManager
from src.chicken_disease_classifier.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException


STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_file()
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        logging.error(e)
        raise CustomException(e,sys)