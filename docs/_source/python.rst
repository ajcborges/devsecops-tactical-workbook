.. include:: global.rst

======
Python
======

An item of note, Python3 is the only choice at this point. Python
2.x End of Life was January 1st, 2020[#]_.

.. [#] https://github.com/python/devguide/pull/344 

.. index::
   single: Python3

Directory Structure
===================

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/franklin" [shape=folder];
      "cloudlab" [shape=folder];
      "python" [shape=folder];
      "/home/franklin" -> "cloudlab" -> "python";
   }