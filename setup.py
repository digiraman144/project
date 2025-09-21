from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements.txt file 
    and returns a list of required packages.
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="project",
    version="0.0.1",
    author="Raman",
    author_email="digiraman144@gmail.com",
    packages=find_packages(where="src"),  # This tells setuptools where to find the packages
    package_dir={"": "src"},  # Specify the directory of the packages
    install_requires=get_requirements("requirements.txt")
)
