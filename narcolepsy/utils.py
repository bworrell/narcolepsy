import dis
import inspect

from . import constants

def classname(cls):
    if not inspect.isclass(cls):
        cls = cls.__class__
    return cls.__name__


def code(func):
    return func.__code__


def numlines(func):
    lines = tuple(dis.findlinestarts(code(func)))
    first_line = lines[0][1]
    last_line  = lines[-1][1]
    return last_line - first_line + 1


def chance(func):
    if not func:
        return constants.DEFAULT_CHANCE

    val = int(0.6 * numlines(func))
    return val if val > 0 else constants.DEFAULT_CHANCE
