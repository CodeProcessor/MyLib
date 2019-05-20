'''
Created on May 20, 2019

@author: dulan
'''
from setuptools import setup, find_packages
import mylib

setup(name='mylib',
      version=mylib.__version__,
      url='https://github.com/DulanGit/MyLib',
      license='MIT',
      author='Dulan Jayasuriya',
      author_email='dulanjayasuriya@gmail.com',
      description='This package is written to easily accessible custom python packages',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)