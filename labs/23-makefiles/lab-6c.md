### Colorizing Makefile Output (Lab 6c)

To add color to our Makefile output we need to define our list of colors
we want to use.

    # Used for colorizing output of echo messages
    BLUE := "\\033[1\;36m"
    LBLUE := "\\033[1\;34m"
    LRED := "\\033[1\;31m"
    YELLOW := "\\033[1\;33m"
    NC := "\\033[0m" # No color/default

We can create a small Makefile to demonstrate the usage of the colors. The
`NC` or ``no color'' option is used to stop colorization of text output.

    code:
            @echo "$(YELLOW)this $(LBLUE)is a $(NC)test."

Running the `make code` command will result in printing our colorized output. 

Next let's define some reusable directives for printing colorized output. 

    print-error:
            @:$(call check_defined, MSG, Message to print)
            @echo -e "$(LRED)$(MSG)$(NC)"

    print-status:
            @:$(call check_defined, MSG, Message to print)
            @echo -e "$(BLUE)$(MSG)$(NC)"

These reusable directives can now be called from other directives. 

    iscontainer: 
            @if [ ! -f /.dockerenv ]; then $(MAKE) print-error MSG="***> This is not a docker container. <***" && exit 1; fi
    checkit:
            $(MAKE) print-status MSG="This is a status message."  
            $(MAKE) print-error MSG="This is an error message."

