##
## EPITECH PROJECT, 2023
## Makefile
## File description:
## Makefile
##

PYTEST		=	pytest

OMIT		=	--omit=*__init__.py,$(SRC_DIR)main.py

SRC_DIR		=	../src/

all:
	coverage run $(OMIT) --source=$(SRC_DIR) -m $(PYTEST) *.py
	coverage report
	coverage html

clean:
	$(RM) -r __pycache__
	$(RM) -r .pytest_cache
	$(RM) -r htmlcov
	$(RM) .coverage

.PHONY: all clean
