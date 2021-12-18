## Docker and Volumes (Lab 4d)

1. Create a [docker-compose.yml file](https://github.com/devsecfranklin/devsecops-tactical-workbook/blob/main/labs/ch4/docker-compose-lab-4d.yml).

1. Create a [Dockerfile](https://github.com/devsecfranklin/devsecops-tactical-workbook/blob/main/labs/ch4/Dockerfile.lab4d).

1. Run the `docker-compose` command to build the image. 

    docker-compose -f docker-compose-lab-4d.yml build volumelab

You should see a message like so: 

    Successfully built 04ae0250dc3c
    Successfully tagged volumelab:latest

You can verify the image built properly like so: 

    docker image ls | grep volumelab

1. Run the `docker-compose` command to get a ``ash'' shell on the image. 

    docker-compose -f docker-compose-lab-4d.yml run volumelab /bin/ash

Note your prompt will change and you will be ``inside'' the containerized development environment. 

    ~ $ pwd
    /home/kflynn
    ~ $ 

1. Use the ls command to show that your filesystem has been mounted on your container.

1. You are a non-privileged user at this point. To escalate your privileges, use ``doas'':

    ~ $ doas apk add --no-cache byacc  
    (1/1) Installing byacc (20210808-r0)  
    Executing busybox-1.34.1-r3.trigger  
    OK: 149 MiB in 52 packages  
    ~ $ 
 
1. Try creating a file.

    touch regularjoe.txt

1. Try creating a file as a member of the ``wheel'' group.

    doas touch bigwheel.txt

1. Finally, exit from the container and verify you can see that your work was written back 
   to the host filesystem.

    ~ $ exit
    ls -la *.txt 
    -rw-r--r-- 1 root     root 0 Dec 18 09:22 bigwheel.txt
    -rw-r--r-- 1 kflynn engr 0 Dec 18 09:22 regularjoe.txt

1. Clean up.

    docker system prune -f && docker image prune -f

