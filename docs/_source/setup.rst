.. include:: global.rst

============
Introduction
============

.. image:: ../images/sky-690293_1920.jpg
   :align: center

At the time of this writing in 2020, about 40% of production workloads are 
running on containers and serverless deployments.  Bare metal and virtual machines currently host 
a bit over 60% of production workloads. Containerized workload use is expected to 
increase in the coming years. Conversely, bare metal and VM usage is expected 
to decrease.[#]_. It's not a question of if, but how quickly commoditization of 
compute resources takes place, leaving only a few main providers of these resources.
This is not unlike how power generation and distribution became centralized, now
the domain of a few large utility companies. Nothing beyond considerations of 
practicality stop you from making your own electricty, but you may wish to invest
your time in other pursuits.

.. [#] https://start.paloaltonetworks.com/esg-research-cloud-native-devsecops-report.html 

In this book, we will explore a combination of techniques that can refresh
your skills and align your projects with current software development techniques. 
We can use small bits and pieces from various technolgies to create a secure build 
pipeline for our lab and development work, test, and even production environments.

We have a goal in mind of selecting complementary tools and process to construct 
and streamline our ways of working. We will attempt to leverage these ways to 
get us quickly and securely to a working lab environment. At the same time we 
should strive for simplicity and reduction of complexity whenever possible.
Complexity in our processes beome the snags and side projects that are the enemy 
of productivity. Refuse to shave more yaks than absolutely necessary!

*****
Setup
*****

To follow along with the examples in this book you will need a host running
a recent version of Linux, or another UNIX variant. An Apple laptop
would also be a good choice. Other operating systems may work as well,
if they have the ability to run a BASH shell, install open source 
packages, etc. Support for environments other than Linux or Mac are
beyond the scope of this book.

Let's take a look at some of the foundational elements it will take to 
make us scuccessful.

The Workhorse (IDE)
===================

I find it extremely helpful to have an Integrated Development Environment
(IDE) that I don't have to spend a lot of time configuring. Lately that 
is Visual Studio Code[#]_. for me. It works well on both Linux and Mac. The 
environment is easily extensible to support most any language, linter, or
syntax checker I might need. 

.. [#] https://code.visualstudio.com/Download

There are times I catch myself switching between VSCode and a terminal
window to do a quick edit in vi or interact with GitHub. Over time I am 
changing the way I work in an attempt to reduce attempts to refocus 
between windows on my desktop.

Work Area
=========

Take a look at the area around your keyboard and make an honest attempt 
to clear away as many distractions as possible. Decluttering your desk will 
help you clear your mind and focus on your projects. 

SSH Key Setup
=============

Take a few minutes to generate an SSH key pair if you don't already have one.
We will be using it at various stages to log in to various sites and hosts. 
The directions for generating an SSH keypair found on the github.com website[#]_ 
are perfect for this task.

.. [#] https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

.. index::
   single: SSH keys

We will save a copy of the file `/home/franklin/.ssh/id_rsa.pub` into a new file
called `/home/franklin/.ssh/authorized_keys`. We will use this file later for logging
in to hosts we build.

GPG Key Setup
=============

Using a GPG key to sign your commits[#]_. will help other verify that work
you check in to revision control did actually come from you. 

.. [#] https://help.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key

.. index::
   single: GPG key

Directory Structure
===================

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: File system layout
   :align: center

   digraph folders {
      "/home/franklin" [shape=folder];
      ".ssh" [shape=folder];
      ".gpg" [shape=folder];
      "/home/franklin" -> ".ssh";
      "/home/franklin" -> ".gpg";
   }