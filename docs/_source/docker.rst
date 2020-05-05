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

Using Docker also gives us the benefit of being able to switch 
quickly between base OS images with just a few lines of change
to our project.
