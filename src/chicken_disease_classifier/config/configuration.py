from src.chicken_disease_classifier.constants import *  # noqa: F403
from src.chicken_disease_classifier.utils import read_yml,create_directories
from src.chicken_disease_classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath= CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH)->None:
        
        self.config=read_yml(config_filepath)
        self.params=read_yml(params_filepath)
        
        create_directories([self.config.artifacts_root])
        
    
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config= DataIngestionConfig(
            root_dir=config.root_dir,
            sourcl_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config