import os

from ExtensionClass import Base


class ComputedAttribute(Base):
    """ComputedAttribute(callable) -- Create a computed attribute"""

    def __init__(self, func, level=0):
        if level > 0:
            func = ComputedAttribute(func, level - 1)
        self.callable = func
        self.level = level

    def __of__(self, inst):
        func = self.__dict__['callable']
        if self.level:
            return func
        return func(inst)


if 'PURE_PYTHON' not in os.environ:  # pragma no cover
    try:
        from ._ComputedAttribute import *
    except ImportError:
        pass
