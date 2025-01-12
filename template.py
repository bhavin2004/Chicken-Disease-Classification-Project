import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)


project_name = "chicken_disease_classifier"

list_of_files = [
    'src/__init__.py',
    f'src/{project_name}/__init__.py',
    f'src/exception.py',
    f'src/logger.py',
    f'src/{project_name}/components/__init__.py',
    # f'src/{project_name}/components/',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/pipelines/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    'app.py',
    'templates/index.html'
]



for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,file_name=os.path.split(filepath)
    
    if file_dir!="" :
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating Directory: {file_dir} for the file:{file_name}")
    
    if (not os.path.exists(filepath)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
        
    else:
        logging.info(f'{file_name} is already exist')
        
        