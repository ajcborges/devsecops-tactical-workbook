.. include:: global.rst

===================================
Continuous Integration & Deployment
===================================

.. image:: ../images/finland-905712_1920.jpg
   :align: center

Accomodations for Continuous Integration (CI) & Continuous Deployment (CD) in our projects
directly corresponds to our chances of success.


.. index::
   single: CI
   single: Continuous Deployment
   single: CD 
   single: Continuous Integration
   

*******
Linters
*******

There are small programs for most (every?) language that you can run before
pushing your changes to GitHub that will catch syntactical and sometimes even
programmatic issues. Consider Python, which is very sensitive with regard to 
indentation. You can programatiacally detect and even correct issues before your
work gets too far down the pipe. This is also a good way to make sure folks
are not committing dirty code to your repositories.

.. index::
   single: lint
   single: linters
   
Here are some of the linters I have found useful for languages I encounter frequently.

.. list-table:: Linters
   :header-rows: 1

   * - Language
     - Name
     - Source
   * - Ansible
     - ansible-lint
     - python (pip install ansible-lint)
   * - Markdown
     - mdl
     - ruby (gem install mdl)
   * - Puppet
     - puppet-lint
     - ruby (gem install puppet-lint) [#]_
   * - Python
     - pylint/flake8
     - python (pip install pylint/flake8)
   * - Terraform
     - tflint
     - https://github.com/terraform-linters/tflint

.. [#] http://puppet-lint.com/


**********
Validaters
**********

packer
terraform

**************
GitHub Actions
**************

GitHub Actions 

.. index::
   single: GitHub Actions

Docker
======

Python
======

Packer
======

Markdown
========

********
TravisCI
********

Travis CI is a hosted continuous integration service used to build and 
test software projects hosted at GitHub and Bitbucket. They have a great
tutorial available [#]_ if you care to dig a bit deeper.

.. [#] https://docs.travis-ci.com/user/tutorial/

By enabling Travis CI integration through the GitHub Marketplace [#]_ you can
integrate their scanners with your repository.

.. [#] https://github.com/marketplace/travis-ci

.. index::
   single: Travis CI

Docker
======

Remember that you can test full Docker containers in your CI/CD pipeline. I 
added these lines to a file named `.travis.yml` to enable automatic molecule 
testing of ansible roles in Travis CI. I also set a flag in the repo settings 
that prevent the PR from being merged until Travis CI flags the build as passing.

.. code-block:: yaml

    ---
    sudo: required
    dist: xenial   # required for Python >= 3.7
    language: python
    services: 
      - docker
    python:
      - "3.7"
      - "3.8"
    before_install:
      - sudo apt-get -qq update
      - python3 -m pip install wheel
      - python3 -m pip install -rrequirements.txt
      - python3 -m pip install -rrequirements-test.txt
    script: 
      - cd playbooks/roles/webserver && molecule test

The contents of the requirements files and the example Ansible code is 
available in the cloudlab repo.

Markdown
========

Save these lines to a file named `.travis.yml` to scan all the markdown
files in your repository.

.. code-block:: yaml

    ---
    sudo: required
    services:
      - docker    
    before_install:
      - sudo apt-get -qq update
      - gem install mdl --no-ri --no-rdoc
    script:
      - mdl -c .mdlrc .

You can also create an `.mdlrc` file to give `mdl` direction on what to scan for.

.. code-block:: shell

    rules "MD001" ,"MD002" ,"MD003" ,"MD004" ,"MD005" ,"MD006" ,"MD007" ,"MD009" ,"MD010" ,"MD011" ,"MD012" ,"MD014" ,"MD018" ,"MD019" ,"MD020" ,"MD021" ,"MD022" ,"MD023" ,"MD025" ,"MD026" ,"MD027" ,"MD028" ,"MD029" ,"MD030" ,"MD031" ,"MD032" ,"MD034" ,"MD035" ,"MD036" ,"MD037" ,"MD038" ,"MD039" 

.. raw:: latex

    \clearpage

*******************
Directory Structure
*******************

Relevant folders and files related to our build pipeline are shown below. The
users home directory and `workspace` subdirectory is implied and removed 
from the diagram for clarity.

.. graphviz::
   :caption: GitHub Actions
   :align: center

   digraph folders {
      "cloudlab" [shape=folder];
      ".github" [shape=folder];
      "workflows" [shape=folder];
      "docker_compose.yml" [shape=rectangle];
      "packer.yml" [shape=rectangle];
      "python.yml" [shape=rectangle];
      "markdown.yml" [shape=rectangle];
      ".travis.yml" [shape=rectangle];
      ".mdlrc" [shape=rectangle];
      "cloudlab" -> ".github";
      "cloudlab" -> ".mdlrc";
      "cloudlab" -> ".travis.yml";
      ".github" -> "workflows";
      "workflows" -> "docker_compose.yml";
      "workflows" -> "markdown.yml";
      "workflows" -> "packer.yml";
      "workflows" -> "python.yml";
   }
