from setuptools import setup, find_packages
from typing import List


hypen_e_dot = "-e ."


def get_requirements(file_path: str = "requirements.txt") -> List[str]:
    """Function will return a list of requirements used for the project"""
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if hypen_e_dot in requirements:
            return [req for req in requirements if req != hypen_e_dot]


setup(
    name="ml-project-1",
    version="1.0.0",
    author="Vivek Sirwal",
    author_email="viveksirwal@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
