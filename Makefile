start:
	python DynaMo.py
v:
	python DynaMo.py -v
clean:
	@rm -v *.pyc *.pyo moduly/*.pyc moduly/*.pyo
patch:
	@echo "aby zaktualizowac, wpisz w konsoli: patch -p1 < (nazwa_latki).patch"

