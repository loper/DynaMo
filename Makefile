start:
	python3.2 DynaMo.py
v:
	python3.2 DynaMo.py -v
clean:
	@rm *.pyc *.pyo moduly/*.pyo moduly/*.pyc *.bak moduly/*.bak *.rej moduly/*.rej 
patch:
	@echo "aby zaktualizowac, wpisz w konsoli: patch -p1 < (nazwa_latki).patch"
