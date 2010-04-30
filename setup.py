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
from setuptools import setup, find_packages, Extension

README = open('README.txt').read()
CHANGES = open('CHANGES.txt').read()

setup(name='ExtensionClass',
      version = '2.13.1',
      url='http://pypi.python.org/pypi/ExtensionClass',
      license='ZPL 2.1',
      description='Metaclass for subclassable extension types',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      long_description='\n\n'.join([README, CHANGES]),

      packages=find_packages('src'),
      package_dir={'': 'src'},

      ext_modules=[Extension("ExtensionClass._ExtensionClass",
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
                   ],
      include_package_data=True,
      zip_safe=False,
      )
