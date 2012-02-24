start:
	python3.2 DynaMo.py
clean:
	@rm -fr __pycache__ moduly/__pycache__ *.bak moduly/*.bak *.rej moduly/*.rej moduly/*.pyc *.pyc testy/*.pyc
	@echo "wyczyszczono"
patch:
	@echo "aby zaktualizowac, wpisz w konsoli: patch -p1 -N < (nazwa_latki).patch"
