### Adding a `make clean` Rule to Your Makefile (Lab 6b)

Let's start by creating a new, blank Makefile. 

    touch Makefile

In this file, we will create a directive called `clean`. We will add an echo to tell 
the user what is happening. Note that the echo line is prepended with an ampersand 
character. Also recall that we must indent the Gnu Makefile using the Tab character.

    clean:
            @echo "Clean up project build files"


Now let's try adding some useful clean up commands. This command is also indented using
the Tab character. Let's try this command without the ampersand so we can see the
optput from the docker command.

            docker system prune -f # remove the stale/temp Docker images

Since we use the Python language often, let's try to find and remove some of it's
related build artifacts.

            @find . -name '*.pyc' | xargs rm -rf
            @find . -name '__pycache__' | xargs rm -rf

Another idea would be to find and remove all items from the filesystem that are found
in a user provided list.  First let's create some files that we can use to verify our
cleanup is working correctly.

    touch file1; touch file2; mkdir dir1

Now let's update our Makefile like so: 

        MY_TRASH_FILES = file1 file2 dir1
        clean:
            @echo "Clean up project build files"
            docker system prune -f # remove the stale/temp Docker images
            @find . -name '*.pyc' | xargs rm -rf
            @find . -name '__pycache__' | xargs rm -rf
            @for trash in $(MY_TRASH_FILES); do \
                    if [ -f $$trash ] || [ -d $$trash ]; then \
                            rm -rf $$trash ; \
                    fi ; \
            done

We have added a new first line, declaring a variable called `MY_TRASH_FILES`. This variable
is a list of files and directories we are interested in removing periodically. The last five
lines of the Makefile are now a for loop that will iterate over the strings in our list. Now
the `make clean` command will look for the list items and remove them each time the 
directive is called. Notice that the reference to the list variable is in parenthesis. Also
note that the `trash` variable in the for loop is referenced with double dollar signs.

