#-*- coding: utf-8 -*-

import logging
import os
import re
import sys

import Menu

class Moduly:

    __zaladowane_obiekty = []
    __zaladowane_pluginy = []

    def __init__(self):
        pass

    def wczytaj_moduly(self):
        """dynamiczne wczytywanie i szukanie pluginow"""
        menu = Menu.Menu()
        logging.debug("[%s] loaded", 'Menu')

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
                logging.error("[%s] Error: %s", i, e)
                del(sys.modules[nazwa])

            """dodawanie do menu głównego"""
            do_menu = obiekt.do_menu()
            #nazwa = nazwa + " (ver. %s)" % obiekt.wersja()
            menu.dodaj_do_menu(do_menu)
            self.__zaladowane_pluginy.append(nazwa)
            self.__zaladowane_obiekty.append((do_menu[0], obiekt))
            logging.debug("[%s] plugin loaded", i)
        menu.dodaj_wyjscie()
        #TODO: konflikty w numeracji w menu
        self.__sprawdz_zaleznosci(menu)
        self.__sprawdzanie_numeracji(menu)
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

    def __sprawdz_zaleznosci(self, menu):
        tmp = dict(self.__zaladowane_obiekty)
        #to c moze kiedys nie dzialac
        c = 0
        for i in tmp:
            c += 1
            obiekt = tmp[i]
            zal = obiekt.zaleznosci()
            for j in zal:
                nazwa = 'moduly.' + j
                """pustych nie sprawdzaj"""
                if obiekt.zaleznosci() == '': continue
                try:
                    assert(sys.modules.get(nazwa) != None)
                except Exception:
                    wadliwy_modul = str(obiekt).split('.')[1]
                    logging.error("[%s] Dependency error: \'%s\'. Module disabled", wadliwy_modul, j)
                    del(sys.modules['moduly.' + wadliwy_modul])
                    del obiekt
                    del zal
                    self.__zaladowane_obiekty.pop(c)
                    self.__zaladowane_pluginy.pop(c)
                    menu.usun_pozycje(i)

    def __sprawdzanie_numeracji(self, menu):
        pozycje = menu.przekaz_pozycje()
        ost = 0
        do_zamiany = []
        wolne = range(0, 10 + 1)
        for k, v in pozycje:
            print k
            if k == ost:
                do_zamiany.append((k, v))
            ost = k

        sys.exit(-1)