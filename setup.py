'''
The setup file provides the essential information related to the packaging and distributing of Python projects. 
It will be used by setuptools(distools) to define the configuration of the project, such as metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of packages from the requirements file.
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file.
            lines = file.readlines()
            # Process each line.
            for line in lines:
                requirement = line.strip()
                ## Ignore the empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="CyberSecurity",
    version='0.0.1',
    author="Danish Ahmed",
    packages=find_packages(),
    install_requires=get_requirements()
)