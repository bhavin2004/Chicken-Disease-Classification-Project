from src.logger import logging
from src.exception import CustomException
from src.chicken_disease_classifier.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline
import sys



STAGE_NAME = "DATA INGESTION STAGE"

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<")

except Exception as e:
    logging.error(e)
    raise CustomException(e,sys)