from setuptools import setup, find_packages
from typing import List

                                         
                 
                       
                                                                       
                     
                                          


project_name= "ML_Project"
VERSION = "0.0.1"
AUTHOR = "chinna reddy"
DESCRIPTION = "This is our Machine learning pipline buliding session "
HYPHEN_E_DOT='-e .'
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirement_list=[requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)     
        return requirement_list






setup(
name=project_name,   
version=VERSION,   
description=DESCRIPTION,
author=AUTHOR,
packages=find_packages(),
install_requires=get_requirements_list()
)