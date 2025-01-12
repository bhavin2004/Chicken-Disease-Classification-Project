import os
import urllib.request as request
import zipfile
from src.logger import logging
from src.chicken_disease_classifier.utils import get_size
from src.chicken_disease_classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config: DataIngestionConfig)->None:
        self.config = config
        
        
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers=request.urlretrieve(
                url=self.config.sourcl_URL,
                filename=self.config.local_data_file
                )
                logging.info(f"{filename} downloaded with following info: \n{headers}")
        
            else:
                logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logging.error(f"Error occurred in download_file of DataIngestion Class due to=>{e}")
      
     
    def unzip_file(self)->None:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
        
        
                