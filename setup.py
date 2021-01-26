from setuptools import setup, find_packages
import pathlib


# directory containing this file
HERE = pathlib.Path(__file__).parent

# README file text
README = (HERE / 'README.md').read_text()

setup(name='usefulfunctions',
      version='1.0.3',
      description='My collection of useful functions',
      long_description=README,
      author='Lloyd Greensite',
      packages=find_packages(),
      url='https://github.com/pynkfloydfan/UsefulFunctions'
      )