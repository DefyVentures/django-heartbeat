#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


setup(
    name='django-heartbeat',
    version='2016.1.25',
    description=('DevOps ping'),
    long_description='',
    author='',
    author_email='',
    url='tba',
    packages=find_packages(),
    # package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
)