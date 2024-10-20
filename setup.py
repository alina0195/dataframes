from setuptools import setup, find_packages

setup(
    name='common-dataframe',
    version='0.1.0',
    description='Extension for frequently used operations with Pandas DataFrames',
    autor='alina',
    packages=find_packages(include=['common-dataframe']),
    install_requires=['pandas'],
)