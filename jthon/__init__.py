__version__ = '1.0.5'

from .jthon import Jthon


def load(file: str=None, data=None):
    '''Load a file into memory

    Parameters
    -----------
    file : Required[:class:`str`]
            Provide the file you'd like to load into memory, Example; file = jthon.load('test_file')
    '''
    if data is None:
        data = {}
    return Jthon(file, data)
