from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='crawler_epoca_cosmeticos',
    version='1.0.0',
    author='Huila Ribeiro',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests']
)
