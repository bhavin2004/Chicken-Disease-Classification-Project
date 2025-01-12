from src.exception import CustomException
from src.logger import logging
import yaml
from box import ConfigBox,BoxError
from ensure import ensure_annotations

from pathlib import Path
import os
import sys


@ensure_annotations
def read_yml(yml_path: Path) -> ConfigBox:
    """It reads yaml flile and returns CongigBoc(similar to dictionary)"""

    try:
        with open(yml_path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"Yaml file:{yml_path} loaded Successfully")
            return ConfigBox(content)
    except BoxError as e:
        logging.info(f"There is errpr in yaml file=>{e}")
        CustomException(e, sys)
    except Exception as e:
        logging.info("Error occurred in real_yaml due to ", e)
        CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories"""

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file


    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path) / 1024)

    return f"~{size_in_kb} KB"
