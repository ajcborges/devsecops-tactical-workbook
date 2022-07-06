CLOCAL_AMFLAGS = -I config/m4 -I aclocal
ACLOCAL_AMFLAGS = -I config/m4 -I aclocal

dot: 
	for myfile in $(shell ls book/dot/*.dot |cut -f1 -d'.'|uniq); do dot -Txdot $$myfile.dot | $(shell which dot2tex) --figonly > $$myfile.tex;done

python:
	@$(PY39) -m venv _build
	( \
		source _build/bin/activate; \
		_build/bin/python -m pip install --upgrade pip; \
        	_build/bin/python -m pip install tox; \
		_build/bin/python -m pip install -r requirements.txt --no-warn-script-location; \
	)
