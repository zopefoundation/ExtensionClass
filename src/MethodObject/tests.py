##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
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

from doctest import DocTestSuite
import unittest


def test_methodobject():
    """
    >>> from ExtensionClass import Base
    >>> from MethodObject import Method

    >>> class foo(Method):
    ...     def __call__(self, ob, *args, **kw):
    ...         print('called %s %s %s' % (ob, args, kw))

    >>> class bar(Base):
    ...     def __repr__(self):
    ...         return "bar()"
    ...     hi = foo()

    >>> x = bar()
    >>> hi = x.hi
    >>> hi(1,2,3,name='spam')
    called bar() (1, 2, 3) {'name': 'spam'}
    """


class TestMethodObject(unittest.TestCase):

    def test_compilation(self):
        from MethodObject import IS_PYPY, IS_PURE
        if IS_PURE or IS_PYPY:
            with self.assertRaises((AttributeError, ImportError)):
                from MethodObject import _MethodObject
        else:
            from MethodObject import _MethodObject
            self.assertTrue(hasattr(_MethodObject, 'Method'))


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(DocTestSuite())
    suite.addTest(unittest.makeSuite(TestMethodObject))
    return suite
