#!/usr/bin/env python

import os
import platform
from pip.download import PipSession
from pip.index import PackageFinder
from pip.req import parse_requirements
from setuptools import setup, find_packages

root_dir = os.path.abspath(os.path.dirname(__file__))

is_pypy = platform.python_implementation() == 'PyPy'
requirements_file = 'pypy.txt' if is_pypy else 'cpython2.txt'
requirements_path = os.path.join(root_dir, 'requirements', requirements_file)

session = PipSession()
finder = PackageFinder([], [], session=session)
requirements = parse_requirements(requirements_path, finder, session=session)
install_requires = [str(r.req) for r in requirements]

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    finder = PackageFinder([], [], session=session)
    requirements_path = os.path.join(root_dir, 'requirements', 'documentation.txt')
    requirements = parse_requirements(requirements_path, finder, session=session)
    install_requires.extend([str(r.req) for r in requirements])

# Hard linking doesn't work inside VirtualBox shared folders. This means that
# you can't use tox in a directory that is being shared with Vagrant,
# since tox relies on `python setup.py sdist`, which uses hard links.
# * https://www.virtualbox.org/ticket/818#comment:94
# * https://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted/22147112#22147112
is_vagrant_vm = 'pinkflamingo-vagrant' in os.path.abspath(os.path.dirname(__file__))
if is_vagrant_vm:
    del os.link

version = '0.1'

setup(
    name="pinkflamingo",
    version=version,
    packages=find_packages(),
    zip_safe=False,
    description="",
    long_description="""\
""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    dependency_links=[
        'http://pypi.safaribooks.com/packages/',
    ],
    url='',
    license='',
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
    # -*- Entry points: -*-
    """,
)
