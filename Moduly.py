#-*- coding: utf-8 -*-
import logging
import os
import re

import Menu

class Moduly:

    __zaladowane_obiekty = []
    __zaladowane_pluginy = []

    def wczytaj_moduly(self):
        """dynamiczne wczytywanie i szukanie pluginow"""
        menu = Menu.Menu()
        logging.debug("[%s] %s loaded", 'program', 'Menu')

        lista_plikow = os.listdir('moduly')
        py = re.compile("\.py$")
        pliki = filter(py.search, lista_plikow)
        nazwa_na_modul = lambda f: os.path.splitext(f)[0]
        nazwy_modulow = map(nazwa_na_modul, pliki)

        for i in nazwy_modulow:
            if i == '__init__': continue
            """pluginy"""
            mod = __import__('moduly.%s' % i)
            """modul"""
            mod = getattr(mod, i)
            nazwa = mod.__name__
            """obiekt"""
            mod = getattr(mod, i)
            obiekt = mod()
            """sprawdzanie poprawności modułu -
               obowiązkowe funkcje: info, wersja, menu, do_menu"""
            try:
                assert(obiekt.info != None)
                assert(obiekt.wersja != None)
                assert(obiekt.menu != None)
                assert(obiekt.do_menu() != None)
            except Exception, e:
                logging.error("[%s] Error loading \"%s\": %s", 'module', i, e)
                continue

            """dodawanie do menu głównego"""
            do_menu = obiekt.do_menu()
            #nazwa = nazwa + " (ver. %s)" % obiekt.wersja()
            menu.dodaj_do_menu(do_menu)
            self.__zaladowane_pluginy.append(nazwa)
            self.__zaladowane_obiekty.append((do_menu[0], obiekt))
            logging.debug("[%s] %s plugin loaded", 'modules', i)
        menu.dodaj_wyjscie()
        #TODO: zaleznosci miedzy modulami
        #TODO: konflikty w numeracji w menu
        return menu
        
    
    def podaj_zaladowane(self):
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
        print "0. POWRÓT"

        self.__wybor_menu()

    def __wybor_menu(self):
        while(1):
            opcja = raw_input('opcja > ')
            try:
                opcja = int(opcja)
            except Exception:
                print "Błędna opcja"
                continue
            if opcja == 0:
                return
            elif opcja == 1:
                self.__wypisz_zaladowane()
            elif opcja == 2:
                self.wczytaj_moduly()
                #TODO: menu nie jest przekazywane do uruchom.py
                print "Moduły zostały przeładowane"
            else:
                print "Bledna opcja"
                continue
            self.menu()

        
        

