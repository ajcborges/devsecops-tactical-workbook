# Used for colorizing output of echo messages
BLUE := "\\033[1\;36m"
LBLUE := "\\033[1\;34m"
LRED := "\\033[1\;31m"
YELLOW := "\\033[1\;33m"
NC := "\\033[0m" # No color/default

code:
	@echo "$(YELLOW)this $(LBLUE)is a $(NC)test."

MY_TRASH_FILES =  file1 file2 dir1
clean:
	@echo "clean up the filesystem"
	docker system prune -f
	for trash in $(MY_TRASH_FILES); do \
		if [ -f $$trash ] || [ -d $$trash ]; then \
			rm -rf $$trash ; \
		fi ; \
	done

