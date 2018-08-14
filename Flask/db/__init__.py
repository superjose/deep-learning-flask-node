# When importing packages you can use:
'''
    Each package in Python is a directory which MUST contain a special file called __init__.py. 
    import foo.bar

    Where foo is the directory and bar is the file

    This also works like this:
    from foo import bar

    The __init__.py file can also decide which modules the package exports as the API, 
    while keeping other modules internal, by overriding the __all__ variable, like so:
    __all__ = ["bar"]
'''

from . import db