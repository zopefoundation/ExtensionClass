Changelog
=========

4.2.0 (2017-01-18)
------------------

- Port the C extension to Python 3.

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6, 3.2.

4.1.2 (2015-04-03)
------------------

- Fix calling of `__class_init__` hook by Python implementation.

4.1.1 (2015-03-20)
------------------

- Avoid wrapping ``__parent__`` in pure-Python version.  Matches
  change made to C version in afb8488.  See issue #3.

4.1 (2014-12-18)
------------------

- Housekeeping changes only.

4.1b1 (2014-11-12)
------------------

- Added compatibility with Python 3.4.

4.1a1 (2013-05-04)
------------------

- Added compatibility with Python 3.2 and 3.3 using the Python reference
  implementation.

- Add Python reference implementation. Used by default on PyPy.

4.0 (2013-02-24)
----------------

- Added trove classifiers to project metadata.

4.0a1 (2011-12-13)
------------------

- Don't create wrappers when retrieving parent pointers.

2.13.2 (2010-06-16)
-------------------

- LP #587760: Handle tp_basicsize correctly.

2.13.1 (2010-04-03)
-------------------

- Removed undeclared testing dependency on zope.testing.

- Removed cruft in ``pickle/pickle.c`` related to removed ``__getnewargs__``.

2.13.0 (2010-02-22)
-------------------

- Avoid defining ``__getnewargs__`` as not to defeat the ZODB persistent
  reference optimization. Refs https://bugs.launchpad.net/zope2/+bug/143657.
  In order to take advantage of this optimization, you need to re-save your
  objects.

2.12.0 (2010-02-14)
-------------------

- Removed old build artifacts and some metadata cleanup.

- Added support for method cache in ExtensionClass. Patch contributed by
  Yoshinori K. Okuji. See https://bugs.launchpad.net/zope2/+bug/486182.

2.11.3 (2009-08-02)
-------------------

- Further 64-bit fixes (Python 2.4 compatibility).

2.11.2 (2009-08-02)
-------------------

- Fixed 64-bit compatibility issues for Python 2.5.x / 2.6.x.  See 
  http://www.python.org/dev/peps/pep-0353/ for details.

2.11.1 (2009-02-19)
-------------------

- Initial egg release.
