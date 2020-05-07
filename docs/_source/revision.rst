.. include:: global.rst

================
Revision Control
================

.. image:: ../images/owl-50267_1920.jpg
   :align: center

The ability to organize and store our projects on free websites like 
github.com is fundamental to our workflow. In addition to giving us 
a way to back up our work and store it for free, it allows for 
collaboration. There are several (mostly) free services we can choose 
from including Bit Bucket and Git Lab. For this exercise we will focus 
on the most well known of these, GitHub.

.. index::
   single: revision control

**********
github.com
**********

One of the very first things you should do (after creating an account, 
that is) is to configure two-factor authentication [#]_ (2FA). 

.. [#] https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa

.. index::
   single: two-factor authentication
   single: GitHub

Now let's take a look at two of the key methods of interacting with projects
and other people on github.com. 

Forking and Cloning Repositories
================================

Forking and then cloning your fork is useful when someone else has a project on
github.com that you woudl like to make changes to. Forking a repository means
you are making a copy of that repository to your personal account on the web site.
Next you want to "clone" a copy of your fork to your local machine so that you 
can make the desired changes.

.. graphviz::
   :caption: Forking and Cloning
   :align: center

   digraph forking {
      "Original Repository on github.com" [shape=rectangle];
      "Your fork on github.com" [shape=rectangle];
      "Local Clone" [shape=rectangle];
      "Original Repository on github.com" -> "Your fork on github.com"[arrowhead=normal];
      "Your fork on github.com" -> "Local Clone"[arrowhead=normal];
      "Local Clone" -> "Original Repository on github.com"[arrowhead=normal label="add remote called upstream"];
   }

This can be a tricky pattern to master, but it is fundamental if you want
to join the ranks of Open Source contributors and developers that enjoy 
the full power of Git.

Steps:
******

- From their project page on github.com, click the "fork" button.
- Now from your page, make a clone of that fork from github.com to your machine.
- On your local machine, create a "remote" connection back to the original repo.

To create a "remote" called `upstream` from your clone to the original repo, 
use this example command:

.. code-block:: bash

   git remote add upstream git@github.com:hotpeppersec/cloudlab.git


After completing these steps you can easily submit pull requests (PRs)
back to the original project.

Creating Repositories
=====================

Directory Structure
===================

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/secdevops" [shape=folder];
      "workspace" [shape=folder];
      "cloudlab" [shape=folder];
      "/home/secdevops" -> "workspace";
      "workspace" -> "cloudlab";
   }