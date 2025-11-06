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

from setuptools import Extension
from setuptools import setup


# PyPy won't build the extension.
if platform.python_implementation() == 'PyPy':
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

# See pyproject.toml for package metadata
setup(ext_modules=ext_modules)
