import os   #os module is useful to perform operating system related tasks, allows perform file,directory,envirenment_variable related operations and more           

from pathlib import Path
import logging  #It's an python liabararies used to know behaviour of your python programme, tracking down issues,check code runs smoothly
                #helpful for maintaining and debugging yur python code

logging.basicConfig(level=logging.INFO)

project_name='env'

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training.py",
    f"src/{project_name}/pipelines/prediction.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    #"Dockerfile",
    #"requirenments.txt",
    #"setup.py",
    #"app.py"    
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir ,filename =os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating_dir:{filedir} for the filename:{filename}")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath)==0)):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")


    else:
         logging.info(f"{filename} is already exist")