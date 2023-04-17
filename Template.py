

import os
import sys
from pathlib import Path
import logging



while True:
    Project_name = input("Enter the Project_name")

    if Project_name !="":
        break

logging.basicConfig(  
    level=logging.INFO,
    format="[%(asctime)s:  %(levelname)s: %(message)s]"
)

list_of_files=[

    f"{Project_name}/__init__.py",
    f"{Project_name}/components/__init__.py",
    f"{Project_name}/config/__init__.py",
    f"{Project_name}/constant/__init__.py",
    f"{Project_name}/entity/__init__.py",
    f"{Project_name}/logger/__init__.py",
    f"{Project_name}/pipeline/__init__.py",
    f"{Project_name}/utiles/__init__.py",
    f"{Project_name}/exception/__init__.py",
    f"config/config.yaml",
    f"setup.py",
    f"main.py",
    f"requirement.txt",
    f"demo.py"

]



for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir ,file_name = os.path.split(file_path):
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True):
        logging.info(f" created new directory at:{file_dir} for file{file_name} ")

    if(not os.path.exists(file_path) or os.path.getsize(file_name)==0):

        with open(file_path,"w") as f:
            pass
            logging.info(f" created new file at:{file_dir} for file: {file_name} ")
    else:
        logging.info(f" The file is aleardy present : {file_name} ")



