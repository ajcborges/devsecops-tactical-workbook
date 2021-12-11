## Testing Out Docker (Lab 4a)

_NOTE_ [Install Docker](https://docs.docker.com/get-docker/) if you haven't already done so.  

For our first container lab, let's get some files in place that will allow us to make sure our setup is all 
working properly. Also we can use these files for subsequent labs.   


1. Create a ``devsecops'' folder on your local machine.  When creating folders, note that capitalization matters.
1. In that folder, create a text file with the name ``Dockerfile''.
1. Copy and paste [the example Dockerfile from earlier in this chapter](https://github.com/devsecfranklin/devsecops-tactical-workbook/blob/main/book/code/21-docker/Dockerfile) into your text file.
1. Create another text file with the name ``docker-compose.yml''
1. Copy and paste [the example docker-compose.yml file from earlier in this chapter](https://github.com/devsecfranklin/devsecops-tactical-workbook/blob/main/book/code/21-docker/docker-compose.yml) into your second text file.
1. Now test like so in Mac/Linux:

```
docker build -t frank378:lab4a - < Dockerfile
```

Test like so in Windows/Powershell:

    Get-Content Dockerfile | docker build -

View the container on your machine:

    docker image ls
