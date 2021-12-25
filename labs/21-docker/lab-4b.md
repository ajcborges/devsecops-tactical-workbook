## Linting a Dockerfile with Hadolint (Lab 4b)

Firstly, we install hadolint:

    wget -O hadolint https://github.com/hadolint/hadolint/releases/download/v1.16.3/hadolint-Linux-x86_64 && chmod 755 hadolint

Now we can execute it on our Dockerfile and see the results:

    $ ./hadolint Dockerfile
    Dockerfile:12 DL3020 Use COPY instead of ADD for files and folders
    Dockerfile:14 DL3008 Pin versions in apt get install. Instead of `apt-get install <package>` use `apt-get install <package>=<version>`
    Dockerfile:14 DL3009 Delete the apt-get lists after installing something
    Dockerfile:14 DL3015 Avoid additional packages by specifying `--no-install-recommends`

You can edit the Dockefile to rectify the errors and run hadolint again to validate your changes. 
Once all the errors have been corrected, the hadolint tool returns no output. Here is our updated Dockerfile.

