'''
setup.py file is an essential part of any Python project. 

It is used to specify the metadata and dependencies of the project,
 making it easier for others to install and use the package. In this setup.py file, 
 we will define the necessary information about our project, such as its name, version, author, and required dependencies.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """Reads the requirements.txt file and returns a list of dependencies."""
    
    requirement_lst :List[str]= []
    try:
        with open('requirements.txt','r') as file:
            #read lines
            lines = file.readlines()
            for line in lines:
                requirement= line.strip()

                #ignore the empty lines and -e .

                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst


print(get_requirements())


setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author = "maran",
    author_email = "maharajmaranoff@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
 

# -e . is used to point to the setup.py file
                