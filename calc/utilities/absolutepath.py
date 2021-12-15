# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from pathlib import Path

def absolutepath(filepath):
    """Absolute path"""
    #absolute path
    relative = Path(filepath)
    return relative.absolute()
