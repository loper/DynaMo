import logging
import os
import os.path
import re

class Moduly:

    __zaladowane_obiekty = []
    __zaladowane_pluginy = []

    def wczytaj_moduly(self, menu):
        #dynamiczne wczytywanie i szukanie pluginow
        lista_plikow = os.listdir('moduly')
        py = re.compile("\.py$")
        pliki = filter(py.search, lista_plikow)
        nazwa_na_modul = lambda f: os.path.splitext(f)[0]
        nazwy_modulow = map(nazwa_na_modul, pliki)

        for i in nazwy_modulow:
            if i == '__init__': continue
            mod = __import__('moduly.%s' % i)
            mod = getattr(mod, i)
            self.__zaladowane_pluginy.append(mod.__name__)
            mod = getattr(mod, i)
            obiekt = mod()
            do_menu = obiekt.do_menu()
            menu.dodaj_do_menu(do_menu)
            self.__zaladowane_obiekty.append((do_menu[0], obiekt))
            logging.debug("[%s] %s plugin loaded", 'modules', i)

        return self.__zaladowane_obiekty
    
    def wypisz_zaladowane(self):
        print "ZALADOWANE MODULY:"
        for i in self.__zaladowane_pluginy:
            print '   - ' + i

