"""
Lightflow-Rest
-----

A REST extension for Lightflow.

It adds tasks for common filesystem operations and rsync as well as a trigger task
that watches a folder and starts a new dag based on changes to files and folders.

"""

from setuptools import setup, find_packages
import re

with open('lightflow_rest/__init__.py') as file:
    version = re.search(r"__version__ = '(.*)'", file.read()).group(1)

setup(
    name='Lightflow-Rest',
    version=version,
    description='A REST extension for Lightflow.',
    long_description=__doc__,
    url='https://bitbucket.synchrotron.org.au/projects/DR/repos/lightflow-rest/browse',

    author='The Australian Synchrotron Python Group',
    author_email='python@synchrotron.org.au',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages(exclude=['tests', 'examples']),

    install_requires=[
        'lightflow>=1.0.0',
        'Flask>=0.12.1'
    ],
)
