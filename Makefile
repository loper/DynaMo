start:
	python DynaMo.py
v:
	python DynaMo.py -v
clean:
	@rm *.pyc *.pyo moduly/*.pyo moduly/*.pyc
patch:
	@echo "aby zaktualizowac, wpisz w konsoli: patch -p1 < (nazwa_latki).patch"
