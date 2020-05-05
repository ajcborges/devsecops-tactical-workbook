.. include:: global.rst

================
Revision Control
================

.. image:: ../images/owl-50267_1920.jpg
   :align: center

The ability to organize and store our projects on free websites like 
github.com is fundamental to our workflow. In addition to giving us 
a way to back up our work and store it for free, it allows for 
collaboration.

.. index::
   single: revision control

**********
github.com
**********

One of the very first things you should do (after creating an account, 
that is) is to configure two-factor authentication [#]_. (2FA). 

.. [#] https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa

.. index::
   single: two-factor authentication
   single: GitHub

Forking and Cloning Repositories
================================

Creating Repositories
=====================

Directory Structure
===================

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/franklin" [shape=folder];
      "cloudlab" [shape=folder];
      "/home/franklin" -> "cloudlab";
   }