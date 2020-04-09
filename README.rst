====================================================
 ExtensionClass and ExtensionClass-related packages
====================================================

ExtensionClass
==============

This package provides a metaclass that allows classes implemented in
extension modules to be subclassed in Python.  Unless you need
ExtensionClasses for legacy applications (e.g. Zope), you probably
want to use Python's new-style classes (available since Python 2.2).

ComputedAttribute
=================

This package provides a way to attach attributes to an
``ExtensionClass`` or instance that are computed by calling a
callable.  This works very much like ``property`` known from new-style
classes, except that a ``ComputedAttribute`` can also be attached to
an instance and that it honours ExtensionClass semantics (which is
useful for retaining Acquisition wrappers, for example).

MethodObject
============

This package lets you attach additional "methods" to ExtensionClasses.
These "methods" are actually implemented by subclassing the
``MethodObject.Method`` class and implementing the ``__call__`` method
there.  Instances of those classes will be bound to the instances
they're attached to and will receive that instance object as a first
parameter (after ``self``).
