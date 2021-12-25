### Python Virtual Environments (Lab 7b)

1. Create a new virtual environment. This command will create a new folder with the name of the virtual environment. It will contain a copy of the binaries and libraries required to run Python.

    `python3 -m venv my-venv`

1. Activate the virtual environment.

    `. ./my-venv/bin/activate`

Observe that your shell prompt has changed. It will be prepended with the name of the Python virutal environment.

1. Try installing a module with `pip`. The module will be available while the virtual environment is active.

    `python -m pip install figcow`

1. Test it out. You should get a nice talking cow in your shell.

    `figcow I love python.`

1. Now exit from the virtual environment.

    `deactivate`

1. Test it again. Since we are no longer in an active virtual environment, the module will not be available to us.

    `figcow I love python.`

    `figcow: command not found`

1. Delete the folder containing the virtual environment.

    `rm -rf my-venv/`

