.. include:: global.rst

=====
Tools
=====

We can reduce our mean time to deploy by using tools to prepare and
generate our machine images programatically, and with scripting languages
such as HCL, which Terraform is based on. In this section we examine these
tools in greater depth.

.. index::
   single: Terraform

******
Packer
******

.. index::
   single: Packer

*********
Terraform
*********

Terraform is a tool for building, changing, and versioning infrastructure 
safely and efficiently[#]_. 

.. [#] https://www.terraform.io/intro/index.html

.. index::
   single: Terraform

*******************
Directory Structure
*******************

So far our relevant files and folders are organized like so:

.. graphviz::
   :caption: Project Directory
   :align: center

   digraph folders {
      "/home/franklin" [shape=folder];
      "cloudlab" [shape=folder];
      "python" [shape=folder];
      "docker" [shape=folder];
      "packer" [shape=folder];
      "cloudlab.json" [shape=rect];
      "/home/franklin" -> "cloudlab";
      "cloudlab" -> "python";
      "cloudlab" -> "docker";
      "cloudlab" -> "packer";
      "packer" -> "cloudlab.json";
   }