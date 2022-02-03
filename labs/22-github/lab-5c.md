## Forking and Cloning (Lab 5c) 

The process of performing a pull request (PR) and merging changes is covered fairly
extensively on the Web. Let's take a quick look at how to keep your local clone of
a repository, as well as your clone on github.com, up to date.

1. First we will create a fork of our original repository.
From the original project page on github.com, click the ``fork'' button.
This creates a copy of the original repository on your personal GitHub page.

1. Now from your personal GitHub repository page, make a clone of that fork from 
github.com to your machine.

This will allow you to add, update and test code and documentation without altering
the original project.
     
1. Next we create a remote. On your local machine, create a ``remote'' path back
  to the original repo. Use this example command:

    `git remote add upstream git@github.com:devsecfranklin/devsecops-tactical-workbook.git`

We are adding a new remote named ``upstream''. Now we can easily submit pull
requests (PRs) back to the original project.

1. These are the steps to take to synchronize once your pull request is merged to the main
branch in the main project repository. From the command line on the
machine where your clone resides:

    `git checkout main`  
    `git fetch upstream`  
    `git rebase upstream/main`  
    `git push origin main`  

