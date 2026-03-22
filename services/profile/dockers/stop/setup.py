import os
import re

from setuptools import find_packages, setup


install_requires = [
    'aiohttp<3.7',
    'aioredis<2',
    'async-timeout<4.0,>=3.0',
    'attrs<21',
    'gunicorn<21',
    'marshmallow<3.14',
    'redis<4',
    'webargs<6'
]

setup(
    name='stop',
    version=1,
    description='stop',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
