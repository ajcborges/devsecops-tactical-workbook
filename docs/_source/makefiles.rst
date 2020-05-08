.. include:: global.rst

=========
Makefiles
=========

.. image:: ../images/books-1163695_1920.jpg
   :align: center

A Makefile is a good way to put shorts sets of oft repeated steps 
at the fingertips of the developer. Rather than typing three complicated and 
possibly hard to recall strings to kick off your Docker container, you 
can simply type `make docker` and have everything build as desired. We're 
going to be using GNU Make for our projects.

.. index::
   single: Makefile

*******************
The PHONY Directive 
*******************

If a file or directory exists with the same name as a stanza in the 
Makefile, you will need to specify it under the *PHONY* directive. This
will allow the Makefile to find and run the desired commands.

Consider this example, where we have three directories (docker, docs, 
and python) and we also have three Makefile directives of the same name:

.. code-block:: bash

    .PHONY: docker docs python

*******
Targets
*******

Makefiles are comprised of various targets. This is where the work gets
done. Let's add a target for Docker and a target for Python to make our
lives easier. 

.. code-block:: bash

   docker: python ## build docker container for testing
      echo "Building CloudLab with docker-compose"
      @if [ -f /.dockerenv ]; then \
      printf "***> Don't run make docker inside docker container <***" && exit 1; fi
      docker-compose -f docker/docker-compose.yml build cloudlab
      @docker-compose -f docker/docker-compose.yml run cloudlab /bin/bash

   python: ## setup python3
      if [ -f 'python/requirements.txt' ]; then \
      pip3 install -rpython/requirements.txt; fi

Be sure when you indent in a Makefile that you use tabs, not spaces.
You can use the backslash character to combine two consecutive lines into 
one logical line.

.. raw:: latex

    \clearpage
    
*********************************
Directory Structure with Makefile
*********************************

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/secdevops" [shape=folder];
      "cloudlab" [shape=folder];
      "python" [shape=folder];
      "docker" [shape=folder];
      "ruby" [shape=folder];
      "Makefile" [shape=rect];
      "/home/secdevops" -> "cloudlab";
      "cloudlab" -> "python";
      "cloudlab" -> "ruby";
      "cloudlab" -> "docker";
      "cloudlab" -> "Makefile";
   }