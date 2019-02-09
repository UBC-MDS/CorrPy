#!/usr/bin/env python
from distutils.core import setup

setup(
    name='CorrPy',
    version='v0.0',
    packages=['CorrPy'],
    author_email= 'na',
    license='MIT',
    description='A package for calculating correlation coefficients and covariance matrix',
    url = ['https://github.com/UBC-MDS/CorrPy'],
    keywords = ['Variance', 'Correlation'],
    install_requires=['numpy']
    )