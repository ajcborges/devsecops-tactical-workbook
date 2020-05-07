.. include:: global.rst

======
Docker
======

.. image:: ../images/container-4203677_1920.jpg
   :align: center

With containerization of our projects, we can take advantge of 
immutability [#]_, starting in our development environment, 
to test and even production. Using immutable containers means we
have hosts that are ephemeral. Ephemerality is the concept of 
things being transitory, existing only briefly [#]_. Rather than spending a great 
deal of time patching and upgrading VM's or bare metal, we're 
going to quickly create a new container in place of the old one.

.. [#] https://www.hashicorp.com/resources/what-is-mutable-vs-immutable-infrastructure/
.. [#] https://en.wikipedia.org/wiki/Ephemerality

.. index::
   single: immutability
   single: Ephemerality
   single: Docker

Using Docker also gives us the benefit of being able to switch quickly 
between base OS images with just a few lines of change to our project. See 
the Docker website for instructions on how to install and configure
Docker [#]_ .

.. [#] https://docs.docker.com/get-docker/

**********
Dockerfile
**********

The Dockerfile is the basic unit of containerization. That is to say, our
containers, and the applications they contain, are defined by the Dockerfile.
Each Dockerfile is predicated on a base image, like Debian 10 as shown in 
the example below.

Create a directory called `docker` and a file called `Dockerfile` within
this directory. Note the capitalization of the first letter in the file name.
Some IDE's will key off this file and allow for additional syntax highlighting.

.. code-block:: bash

   FROM debian:buster
   LABEL AUTHOR="franklin@bitsmasher.net"
   ENV DEBIAN_FRONTEND noninteractive

   ADD . /project
   WORKDIR /project

   # env stuff
   RUN apt update; \
   apt -y install apt-utils

******************
docker-compose.yml
******************

The docker compose file allows us to manage multiple Docker containers for
one or more applications. We will add it as part of our framework so we 
are prepared to extend our projects later, as needed.

Create a file called `docker-compose.yml` in our new `docker` directory.

.. code-block:: bash

   version: '3'
   services:
   cloudlab:
      hostname: cloudlab
      container_name: cloudlab
      volumes:
         - ..:/project
      build:
         context: ..
         dockerfile: docker/Dockerfile

**************************
Docker Directory Structure
**************************

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/secdevops" [shape=folder];
      "cloudlab" [shape=folder];
      "python" [shape=folder];
      "docker" [shape=folder];
      "docker-compose.yml" [shape=rect];
      "Dockerfile" [shape=rect];
      "/home/secdevops" -> "cloudlab";
      "cloudlab" -> "python";
      "cloudlab" -> "docker";
      "docker" -> "Dockerfile";
      "docker" -> "docker-compose.yml";
   }