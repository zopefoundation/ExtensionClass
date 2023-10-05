===========
 Changelog
===========

5.1 (2023-10-05)
================

- Add support for Python 3.12.


5.0 (2023-01-19)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Fix deprecation warning in tests.


4.9 (2022-11-17)
================

- Add support for building arm64 wheels on macOS.


4.8 (2022-11-03)
================

- Update Python 3.11 support to the final release.


4.7 (2022-09-16)
================

- Update Python 3.11 support to rc2.

- Disable unsafe math optimizations in C code.
  (`#55 <https://github.com/zopefoundation/ExtensionClass/pull/55>`_)


4.6 (2022-01-14)
================

- Add support for Python 3.10 and 3.11 (as of alpha 3).


4.5.1 (2021-06-11)
==================

- Create wheels for Linux (2010, 2014 and aarch) and MacOS.


4.5.0 (2020-10-07)
==================

- Drop support for Python 3.4.

- Add support for Python 3.8 and 3.9.

- Fix accessing ``__parent__`` when it is defined as a class attribute
  that is ``None`` (e.g., in subclasses of
  ``zope.conatiner.contained.Contained``). See `issue 24
  <https://github.com/zopefoundation/ExtensionClass/issues/24>`_.

4.4.0 (2018-10-05)
==================

- Fail if C extensions couldn't be compiled on compatible platforms.

- Add Appveyor configuration to automate building Windows eggs

- Add support for Python 3.7.

- Fix getting attributes that are data descriptors in the Python
  implementation.

- Reach and automatically maintain 100% test coverage.

4.3.0 (2017-02-22)
==================

- Drop support for Python 3.3.

- Remove unused C macro from ``ExtensionClass.h``.

- Fix C compilation under Windows.

4.2.1 (2017-02-02)
==================

- Fix problems with computed attribute and property wrapping.

4.2.0 (2017-01-18)
==================

- Port the C extension to Python 3.

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6, 3.2.

4.1.2 (2015-04-03)
==================

- Fix calling of ``__class_init__`` hook by Python implementation.

4.1.1 (2015-03-20)
==================

- Avoid wrapping ``__parent__`` in pure-Python version.  Matches
  change made to C version in afb8488.  See issue #3.

4.1 (2014-12-18)
================

- Housekeeping changes only.

4.1b1 (2014-11-12)
==================

- Added compatibility with Python 3.4.

4.1a1 (2013-05-04)
==================

- Added compatibility with Python 3.2 and 3.3 using the Python reference
  implementation.

- Add Python reference implementation. Used by default on PyPy.

4.0 (2013-02-24)
================

- Added trove classifiers to project metadata.

4.0a1 (2011-12-13)
==================

- Don't create wrappers when retrieving parent pointers.

2.13.2 (2010-06-16)
===================

- LP #587760: Handle tp_basicsize correctly.

2.13.1 (2010-04-03)
===================

- Removed undeclared testing dependency on zope.testing.

- Removed cruft in ``pickle/pickle.c`` related to removed ``__getnewargs__``.

2.13.0 (2010-02-22)
===================

- Avoid defining ``__getnewargs__`` as not to defeat the ZODB persistent
  reference optimization. Refs https://bugs.launchpad.net/zope2/+bug/143657.
  In order to take advantage of this optimization, you need to re-save your
  objects.

2.12.0 (2010-02-14)
===================

- Removed old build artifacts and some metadata cleanup.

- Added support for method cache in ExtensionClass. Patch contributed by
  Yoshinori K. Okuji. See https://bugs.launchpad.net/zope2/+bug/486182.

2.11.3 (2009-08-02)
===================

- Further 64-bit fixes (Python 2.4 compatibility).

2.11.2 (2009-08-02)
===================

- Fixed 64-bit compatibility issues for Python 2.5.x / 2.6.x.  See
  http://www.python.org/dev/peps/pep-0353/ for details.

2.11.1 (2009-02-19)
===================

- Initial egg release.
