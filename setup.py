#!/usr/bin/env python3
"""script for instalation of my_owm"""
from setuptools import setup, find_packages

def get_readme():
    """reads README"""
    with open('README.md') as file:
        return file.read()

setup(
    name='drivers-my_owm',
    version='0.1',
    description='Open weather map commandline client',
    long_description=get_readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'requests'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_owm=source.my_owm:main',
        ],
    },
)
