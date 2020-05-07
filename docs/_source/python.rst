.. include:: global.rst

======
Python
======

.. image:: ../images/snake-1634293_1920.jpg
      :align: center

An item of note, Python3 is the only choice at this point. Python
2.x End of Life was January 1st, 2020 [#]_ .

.. [#] https://github.com/python/devguide/pull/344 

.. index::
   single: Python3

*****************
Requirements File
*****************

********************
The __init__.py File
********************

We add this file to let the Python interpreter know that the directories
it is found in are a contiguous part of our project. Since module imports and
function definitions in this file are availabel to all the python code files
in the directory, we can use it to our advantage. For example, try adding this 
quick and dirty logging function to `__init__.py`:

.. code-block:: python

   '''
   Configure logger
   '''
   Path("/var/log/cloudlab").mkdir(parents=True, exist_ok=True)
   logging.basicConfig(
      filename="/var/log/cloudlab/cloudlab.log",
      level=logging.DEBUG,
      format="[%(asctime)s] [%(filename)s:%(lineno)s - %(funcName)5s() - 
      %(processName)s] %(levelname)s - %(message)s"
   )

Now we can create a Python file `log_test.py` and call the logger from 
within like so:

.. code-block:: python

   import logging
   from pathlib import Path
   def main():
      logging.debug('Loggy Loggerton')
   if __name__ == "__main__":
      main()

Check the results in the file `/var/log/cloudlab/cloudlab.log`.

**************************
Python Directory Structure
**************************

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/secdevops" [shape=folder];
      "cloudlab" [shape=folder];
      "python" [shape=folder];
      "requirements.txt" [shape=rect];
      "__init__.py" [shape=rect];
      "/home/secdevops" -> "cloudlab";
      "cloudlab" -> "python";
      "python" -> "__init__.py";
      "python" -> "requirements.txt";
   }