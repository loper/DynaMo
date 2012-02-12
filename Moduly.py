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
            if i == '__init__' or i == 'blank': continue

            """pluginy"""
            mod = __import__('moduly.%s' % i)
            """modul"""
            mod = getattr(mod, i)
            nazwa = mod.__name__
            """obiekt"""
            try:
                mod = getattr(mod, i)
            except Exception, e:
                logging.error("[%s] Error: %s", i, e)
                continue
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
                continue
            """dodawanie do menu głównego"""
            do_menu = obiekt.do_menu()
            nazwa = nazwa + " (ver. %s)" % obiekt.wersja()
            menu.dodaj_do_menu(do_menu)
            self.__zaladowane_pluginy.append(nazwa)
            self.__zaladowane_obiekty.append([do_menu[0], obiekt])
            logging.debug("[%s] plugin loaded", i)
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
        #TODO:problem z wyswietlaniem - albo sie cofa 50 razy albo nie wypisuje menu

    def __sprawdz_zaleznosci(self, menu):
        #tu kiedys byla zamiana na dict
        tmp = self.__zaladowane_obiekty
        #to c moze kiedys nie dzialac
        c = 0
        for i in tmp:
            c += 1
            obiekt = i[1]
            zal = obiekt.zaleznosci()
            for j in zal:
                nazwa = 'moduly.' + j
                """pustych nie sprawdzaj"""
                if obiekt.zaleznosci() == '': continue
                try:
                    assert(sys.modules.get(nazwa) != None)
                except Exception:
                    wadliwy_modul = str(obiekt).split('.')[1]
                    logging.error("[%s] dependency error: \'%s\'. Module disabled", wadliwy_modul, j)
                    del(sys.modules['moduly.' + wadliwy_modul])
                    del obiekt
                    del zal
                    self.__zaladowane_obiekty.pop(c)
                    self.__zaladowane_pluginy.pop(c)
                    menu.usun_pozycje(i[0])
        # wczytalo modul, mimo ze zostal wywalony

    def __sprawdzanie_numeracji(self, menu):
        pozycje = menu.przekaz_pozycje()
        ost = 0
        do_zamiany = []
        oim = self.__obiekty_i_menu()
        wolne = range(0, 9 + 1)
        for k, v in pozycje:
            if k == ost:
                do_zamiany.append(v)
                pozycje.pop(pozycje.index((k, v)))
            else:
                wolne.pop(wolne.index(k))
            ost = k
        do_zamiany.sort()
        #TODO:obiekt pozostal niezmieniony
        for v in do_zamiany:
            nr = wolne.pop(1)
            pozycje.append((nr, v))
            self.__zmien_obiekt(oim.get(v), nr)
        pozycje.sort()
        return menu

    def __obiekty_i_menu(self):
        obj = {}
        for i in self.__zaladowane_obiekty:
            obiekt = i[1]
            do_menu = obiekt.do_menu()[1]
            obj.update({do_menu:obiekt})
        return obj

    def __zmien_obiekt(self, obiekt, nr):
        for i in self.__zaladowane_obiekty:
            if i[1] == obiekt:
                i[0] = nr
                return
