from setuptools import setup,find_packages
from typing import List


def get_requirenments(file_path:str)->List[str]:
      '''this will return list of requirenments'''
      requirenments=[]
      with open(file_path) as file_obj:
        requirenments=file_obj.readlines()
        requirenments=[req.replace('\n',"") for req in requirenments]
        return requirenments








setup(
    name='env',
    version='0.0.1',
    author='krish',
    author_email='sumitnsawant822@gmail.com',
    packages=find_packages(),
    install_requires=get_requirenments('requirements.txt')
)