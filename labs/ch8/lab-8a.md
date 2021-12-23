### Setting up Development Envrinoment with Nix (Lab 8a)

1. Install `nix-shell` on your machine.

    curl -L https://nixos.org/nix/install | sh

1. You should see a message similar to the following:

    Installation finished!  To ensure that the necessary environment
    variables are set, either log in again, or type

        . /home/franklin/.nix-profile/etc/profile.d/nix.sh

    in your shell.

1. You can type `set | grep NIX` to verify the correct environment variables are now set in your shell.

1. The `nix-shell` command will look for a file called `shell.nix` in the current directory. Here is
   an example of how that file should look.

    let  
      pkgs = import <nixpkgs> {};  
    in pkgs.mkShell {  
      buildInputs = [  
        pkgs.python3  
        pkgs.python3.pkgs.pip  
        pkgs.python3.pkgs.setuptools  
        pkgs.python3.pkgs.tox  
        pkgs.python3.pkgs.virtualenv  
      ];   
      src = null;  
      shellHook = ''  
        # Allow the use of wheels.  
        SOURCE_DATE_EPOCH=$(date +%s)   
        export NIX_PATH="nixpkgs=/nix"  
        # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.  
        export PIP_PREFIX=$(pwd)/_build/pip_packages   
        export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH"  
        export PATH="$PIP_PREFIX/bin:$PATH"  
      '';  
    }  

After creating this file in the current directory, type the `nix-shell` command in the same directory.
It will take a few minutes for Nix to install/update all the relevant packages. Your prompt will also 
change to let you know you are now running the Nix shell. 

Try typing `which python` and observe that the Python binary is located in a subdirectory of `/nix/store`.

Finally, let's try installing a Python module using pip:

    python3 -m pip install figcow  
    figcow devsecops  

When you are finished working in the nix-shell, type `exit` to return to your regular shell.

