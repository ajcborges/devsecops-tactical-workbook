.. include:: global.rst

================
Revision Control
================

.. image:: ../images/owl-50267_1920.jpg
   :align: center

The ability to organize and store our projects on free websites like 
github.com is fundamental to our workflow. In addition to giving us 
a way to back up our work and store it for free, it facilitates a greater degree of 
collaboration. There are several (mostly) free services we can choose 
from including Bit Bucket and Git Lab. For this exercise we will focus 
on the most well known of these, GitHub.

.. index::
   single: revision control

**********
github.com
**********

Simply put, github.com is a website that allows you to store the work
you are using git to manage. Git is the tool that allows for revision control 
of your work. GitHub is a repository for storing that work, creating teams 
to work on projects, tracking issues, release snapshotting, and more.

One of the very first things you should do (after creating an account, 
that is) is to configure two-factor authentication [#]_ (2FA) for your GitHub
account. 

.. [#] https://help.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa

.. index::
   single: two-factor authentication
   single: GitHub

Let's take a look at two of the key methods of interacting with projects
and other people on github.com. 

Forking and Cloning Repositories
================================

Forking and then cloning your fork is useful when someone else has a project on
github.com that you would like to make changes to. Forking a repository means
you are making a copy of that repository to your personal account on the web site.
Next you want to "clone" a copy of your fork to your local machine so that you 
can make the desired changes. Adding a "remote" is a way to easily push changes
from your clone back to the original source repository.

.. index::
   single: Forking
   single: Cloning

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
the full power of Git and GitHub.

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

If you are starting out on a new project, simply creating a repo is 
probably enough. Often I will start a repository on my personal account
while I use the steps in this book to get the project of fthe ground.
Later I will move the repository into an organization where the responsibility 
for ownership and administration can be shared with other folks.

While the repository is owned by me, I use a much simpler process for
managing my code check-ins.

Steps
*****

- Create the repository on github.com from my personal account.
- Make a clone of that new repository from github.com to my local host.
- Do my pull requests and merges as desired.
- Do a `git pull` to my master branch to keep my local clone up to date.

CODEOWNERS
==========

Creating a `CODEOWNERS` file [#]_ is a good way to automatically tag folks in PRs
to make them aware of changes to certain files or folders in your projects.

.. [#] https://help.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners

.. index::
   single: CODEOWNERS

In it's most basic form, the CODEOWNERS file in the .github directory simply 
lists the file(s) and the owner(s) on a line together. It looks like this:

.. code-block:: bash

   * @hotpeppersec

In this example, the @hotpeppersec user will be tagged as a reviewer in all pull 
requests.

Repository Settings
===================

Which flags should you flip after clicking on the little gear icon?

.. raw:: latex

    \clearpage

Directory Structure
===================

Relevant files and folders mentioned in this chapter are organized as seen below.

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/secdevops" [shape=folder];
      "workspace" [shape=folder];
      "cloudlab" [shape=folder];
      ".github" [shape=folder];
      "CODEOWNERS" [shape=rectangle];
      "/home/secdevops" -> "workspace";
      "workspace" -> "cloudlab";
      "cloudlab" -> ".github";
      ".github" -> "CODEOWNERS";
   }