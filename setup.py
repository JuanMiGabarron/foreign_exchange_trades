from setuptools import setup, find_packages

setup(
    name='tradeApp',
    version='0.1',
    packages=find_packages(exclude=['tests', 'drivers', 'venv', 'config']),
)
