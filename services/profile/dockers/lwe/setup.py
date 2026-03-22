import os
import re

from setuptools import find_packages, setup


install_requires = [
    'aiohttp<3.7',
    'aiojobs<1',
    'aioredis<2',
    'async-timeout<4.0,>=3.0',
    'attrs<21',
    'gunicorn<21',
    'marshmallow<3.14',
    'numpy<1.20',
    'webargs<6'
]

setup(
    name='lwe',
    version=1,
    description='lwe',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
