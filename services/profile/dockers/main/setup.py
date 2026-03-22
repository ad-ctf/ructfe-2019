import os
import re

from setuptools import find_packages, setup


install_requires = [
    'Flask<2',
    'Jinja2<3',
    'MarkupSafe<2',
    'Werkzeug<2',
    'certifi<2022',
    'click<8',
    'gunicorn<21',
    'redis<4',
    'requests<2.28',
    'urllib3<2'
]

setup(
    name='main',
    version=1,
    description='main',
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
