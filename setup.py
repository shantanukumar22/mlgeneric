from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'

# function to install all the packages from requirements.txt
def get_requirements(file_path:str) -> List[str]:
    """this function will return the list of requirements"""
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
# to prevent the requirements() to read the \n after every line from requirements.txt
        requirements=[req.replace("\n,"," ") for req in requirements]
        # -e . is used to call the setup.py but it should not included to install 
        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="shantanu",
    author_email="shantanuk436@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)