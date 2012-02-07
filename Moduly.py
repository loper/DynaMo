#-*- coding: utf-8 -*-
import logging
import os
import re
import sys

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
            nazwa = mod.__name__
            mod = getattr(mod, i)
            obiekt = mod()
            do_menu = obiekt.do_menu()
            nazwa = nazwa + " (ver. %s)" % obiekt.wersja()
            menu.dodaj_do_menu(do_menu)
            self.__zaladowane_pluginy.append(nazwa)
            self.__zaladowane_obiekty.append((do_menu[0], obiekt))
            logging.debug("[%s] %s plugin loaded", 'modules', i)

        return self.__zaladowane_obiekty
    
    def __wypisz_zaladowane(self):
        print "ZAŁADOWANE MODULY:"
        for i in self.__zaladowane_pluginy:
            print '   - ' + i
        print "\n"


    def menu(self):
        # os.system("clear")
            print "MODULY:"
            print "1. Lista modulów"
            print "2. Przeladuj moduly"
            print "9. WYJŚCIE"

            self.__wybor_menu()

    def __wybor_menu(self):
        while(1):
            opcja = input('opcja > ')
            if opcja == 9:
                sys.exit(0)
            elif opcja == 1:
                self.__wypisz_zaladowane()
            elif opcja == 2:
                self.wczytaj_moduly()
            else:
                print "Bledna opcja"
                continue
            self.menu()

        
        

