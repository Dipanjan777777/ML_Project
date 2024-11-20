from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the requirements.txt file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ML_Project",  # Corrected the project name
    version="0.1.0",  # Initial version
    author="Dipanjan",
    author_email="dipanjansantra2019@gmail.com",
    description="A brief description of your project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
