import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_Name="projectfiles"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_Name}/__init__.py",
    f"src/{project_Name}/components/__init__.py",
    f"src/{project_Name}/components/data_injection.py",
    f"src/{project_Name}/components/data_transformation.py",
    f"src/{project_Name}/components/model_training.py",
    f"src/{project_Name}/components/model_monitoring.py",
    f"src/{project_Name}/pipelines/__init__.py",
    f"src/{project_Name}/pipelines/training_pipeline.py",
    f"src/{project_Name}/pipelines/testing_pipeline.py",
    f"src/{project_Name}/exception.py",
    f"src/{project_Name}/logger.py",
    f"src/{project_Name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt" ,
    "setup.py"         
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if (filedir!=""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating dictionary {filedir} for the file {filename}")
        
        
    if(not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file {filepath}")
    
    else:
        logging.info(f"file {filename} already present Hence skipping the creating the file")
        










