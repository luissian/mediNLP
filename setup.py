# setup.py
from setuptools import setup, find_packages

setup(
    name='MediNLP',
    version='0.1',
    description='A Python package for scraping and analyzing health-related articles',
    author='Your Name',
    author_email='youremail@example.com',
    packages=find_packages(),  # Automatically find the medi_nlp package
    install_requires=[
        'requests',
        'beautifulsoup4',
        'spacy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
