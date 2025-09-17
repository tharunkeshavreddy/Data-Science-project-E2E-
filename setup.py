from setuptools import find_packages,setup
from typing import List


ignore='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function returns the requirements
    '''
    
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
        
        if ignore in requirements:
            requirements.remove(ignore)
            
    
    return requirements


















setup(
    name="Datascienceprj",
    version='0.0.1',
    author='Tharun_Keshav_Reddy',
    author_email='h20240868@pilani.bits-pilani.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )