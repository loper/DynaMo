start:
	python DynaMo.py
v:
	python DynaMo.py -v
clean:
	\rm -v *.pyc *.pyo moduly/*.pyc moduly/*.pyo
patch:
	patch -p1 < *.patch
