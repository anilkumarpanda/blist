from setuptools import setup, find_packages

setup(
    name='blist',
    version='0.1.2',
    url='https://github.com/anilkumarpanda/blist',
    author='Anilkumar Panda',
    description='Package for parsing blog posts',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.6', 
    'pandas >= 0.20.3', 
    'beautifulsoup4 >= 4.6.3', 
    'requests >= 2.18.4', 
    'lxml >= 4.1.1', 
    'bs4 >= 0.0.1'],
)