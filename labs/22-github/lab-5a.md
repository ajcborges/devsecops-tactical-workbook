## Creating A New Repository (Lab 5a)

1. Create the repository on github.com from a personal account. [https://github.com/new](https://github.com/new)
  1. Give the repository a name. (Example will use `devsecops-lab`)
  1. Click the green _Create repository_ button.
1. From the `/home/devsecops/workspace/myproject` directory, run these commands.  Be sure to replace `mygithubusername` with your GitHub username.

    `git init`    
    `git .`  
    `git commit -m "first commit"`  
    `git branch -M main`  
    `git remote add origin git@github.com:mygithubusername/devsecops-lab.git`  
    `git push -u origin main`  

1. On the GitHub website you should be able to reload the page for the repository and see your files in the listing.

