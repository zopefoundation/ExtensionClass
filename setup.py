##############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for the ExtensionClass distribution
"""
import os
import platform
from setuptools import setup, find_packages, Extension

with open('README.rst') as f:
    README = f.read()

with open('CHANGES.rst') as f:
    CHANGES = f.read()

# PyPy won't build the extension.
py_impl = platform.python_implementation
is_pypy = py_impl() == 'PyPy'

if is_pypy:
    ext_modules = []
else:
    ext_modules = [
        Extension("ExtensionClass._ExtensionClass",
                  [os.path.join('src', 'ExtensionClass',
                                '_ExtensionClass.c')],
                  include_dirs=['src']),
        Extension("ComputedAttribute._ComputedAttribute",
                  [os.path.join('src', 'ComputedAttribute',
                                '_ComputedAttribute.c')],
                  include_dirs=['src']),
        Extension("MethodObject._MethodObject",
                  [os.path.join('src', 'MethodObject',
                                '_MethodObject.c')],
                  include_dirs=['src']),
    ]

version = '4.5.0'

setup(
    name='ExtensionClass',
    version=version,
    url='https://github.com/zopefoundation/ExtensionClass',
    license='ZPL 2.1',
    description='Metaclass for subclassable extension types',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    long_description='\n\n'.join([README, CHANGES]),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    ext_modules=ext_modules,
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'test': [
            'zope.testrunner',
        ],
    },
)
