.PHONY: docker docs 

# Used for colorizing output of echo messages
BLUE := "\\033[1\;36m"
NC := "\\033[0m" # No color/default

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
  match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
  if match:
    target, help = match.groups()
    print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: ## Cleanup all the things
	cd docs && make clean && cd -

docker: python ## build docker container for testing
	$(MAKE) print-status MSG="Building with docker-compose"
	@if [ -f /.dockerenv ]; then $(MAKE) print-status MSG="***> Don't run make docker inside docker container <***" && exit 1; fi
	docker-compose -f docker/docker-compose.yml build cloudlab
	@docker-compose -f docker/docker-compose.yml run cloudlab /bin/bash

docs: python ## Generate documentation
	#sphinx-quickstart
	cd docs && make html

print-status:
	@:$(call check_defined, MSG, Message to print)
	@echo "$(BLUE)$(MSG)$(NC)"

python: ## setup python3
	if [ -f 'python/requirements.txt' ]; then pip3 install -rpython/requirements.txt; fi
