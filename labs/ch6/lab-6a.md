### Using PHONY in a Makefile (Lab 6a)

1. Create a small two-line Makefile. Be sure to use a tab character to indent the second line.

    code:
            echo "this is a test"

1. Test the Makefile by running the `make` command. Notice that you can
type `make` or `make code` and get the same result.

    franklin:~$ make code  
    make: 'code' is up to date.  
    franklin:~$ make   
    make: 'code' is up to date.  

1. Now edit the Makefile to include the PHONY directive. Be mindful of the
leading dot character.

    .PHONY: code  
    code:  
            echo "this is a test"  

1. Try running make again.

    franklin:~$ make code  
    echo "this is a test"  
    this is a test   
    franklin:~$   

1. Note that the output occurs twice. To suppress the extra output, you can prepend the command 
   with an ampersand character.

    .PHONY: code
    code:
            @echo "this is a test"

1. Now try running one final time.

    franklin:~$ make code
    this is a test

Now we get the desired result without the printing of the command
by make.

