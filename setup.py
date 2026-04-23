from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Amr Elhefnawy',
    author_email='amr223489@gmail.com',
    package = find_packages(),
    install_requires=get_requirements('requirements.txt')
)