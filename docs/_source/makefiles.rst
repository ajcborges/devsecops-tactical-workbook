.. include:: global.rst

=========
Makefiles
=========

.. image:: ../images/books-1163695_1920.jpg
   :align: center

Makefiles are a good way to put shorts sets of oft repeated steps 
at the fingertips of the dev. Rather than typing three complicated and 
possibly hard to recall strings to kick off your Docker container, you 
can simply type `make docker` and have everything build as desired.

.. index::
   single: Makefile

Basic Layout
------------



The PHONY Directive 
-------------------

If a file or directory exists with the same name as a stanza in the 
Makefile, you will need to specify it under the *PHONY* directive. This
will allow the Makefile to find and run the desired commands.

Consider this example, where we have three directories (docker, docs, 
and python) and we also have three Makefile directives of the same name:

.. code-block:: bash

    .PHONY: docker docs python

