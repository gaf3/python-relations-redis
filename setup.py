#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="relations-redis",
    version="0.1.0",
    package_dir = {'': 'lib'},
    py_modules = [
        'relations_redis
    ],
    install_requires=[
        'redis==3.5.2'
    ]
)
