### Getting Setup for Success (Lab 7a)

1. Install [the latest version of Python for your host OS](https://www.python.org/downloads/) from their website.

1. You may wish to [install the latest Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) to your Visual Studio Code environment.

1. Create an `src` directory.

1. Create a file called `__init__.py` in the `src` directory.

1. Create a file called `__main__.py` in the `src` directory.

    `import sys`

    `print(sys.version)`  
    `print('I like Python')`

1. Test the Python code you created. 

    `python3 -m src`

Note that by creating a ``__main__.py` file, we are are to call the project as a module directly by using the `-m` flag. Although this is not typical, it may be useful to you if you are creating a proper Python module.

