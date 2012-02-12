#-*- coding: utf-8 -*-

"""wyszukuje i dynamicznie wczytuje moduły i tworzy ich obiekty

Modułów szuka w 'moduly/'. Wczytuje je i tworzy listę obiektów, które są
wywoływane z poziomu menu. Dodatkowo wypisuje ich listę i umożliwia
przeładowanie."""

import logging
import os
import re
import sys

import Menu

class Moduly:
    '''klasa Moduly'''

    __zaladowane_obiekty = []
    __zaladowane_pluginy = []

    def __init__(self):
        pass

    def wczytaj_moduly(self):
        '''dynamiczne wczytywanie i szukanie pluginow w folderze "moduly"'''
        menu = Menu.Menu()
        logging.debug("[%s] loaded", 'Menu')

        lista_plikow = os.listdir('moduly')
        pliki_py = re.compile("\.py$")
        znalezione = filter(pliki_py.search, lista_plikow)
        nazwa_na_modul = lambda f: os.path.splitext(f)[0]
        nazwy_modulow = map(nazwa_na_modul, znalezione)

        for i in nazwy_modulow:
            """wszystko, oprócz __init__ i blank"""
            if i in('__init__', 'blank'):
                continue

            """pluginy"""
            mod = __import__('moduly.%s' % i)
            """modul"""
            mod = getattr(mod, i)
            nazwa = mod.__name__
            """obiekt"""
            try:
                mod = getattr(mod, i)
            except AttributeError, err:
                logging.error("[%s] Error: %s", i, err)
                continue
            obiekt = mod()
            """sprawdzanie poprawności modułu -
               obowiązkowe funkcje: info, wersja, menu, do_menu"""
            try:
                assert(obiekt.info != None)
                assert(obiekt.wersja != None)
                assert(obiekt.menu != None)
                assert(obiekt.do_menu() != None)
            except AttributeError, err:
                logging.error("[%s] Error: %s", i, err)
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
        '''zwraca listę załadowanych'''
        return self.__zaladowane_obiekty

    def __wypisz_zaladowane(self):
        '''wypisuje listę załadowanych i ich wersje'''
        print "\nZAŁADOWANE MODULY:"
        for i in self.__zaladowane_pluginy:
            print '   - ' + i

    def menu(self):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print "MODUŁY:"
        print "1. Lista modułów"
        print "2. Przeładuj moduły"
        print "0. POWRÓT"

        self.__wybor_menu()

    def __wybor_menu(self):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = raw_input('opcja > ')
            try:
                opcja = int(opcja)
            except ValueError:
                print "Błędna opcja"
                continue
                
            if opcja == 0:
                return
            elif opcja == 1:
                self.__wypisz_zaladowane()
            elif opcja == 2:
                self.__zaladowane_obiekty = []
                self.__zaladowane_pluginy = []
                self.wczytaj_moduly()
                #menu nie jest przekazywane do uruchom.py - BŁĄD!!!!!!!!!!!!!!!!!!!!!!!!!!
                print "Moduły zostały przeładowane"
            else:
                print "Błędna opcja"
                continue
        self.menu()

    def __sprawdz_zaleznosci(self, menu):
        '''sprawdza, czy spełnione są zależności między modułami
        i ewentualnie wyłącza "złe" moduły'''
        tmp = self.__zaladowane_obiekty
        #to c moze kiedys nie dzialac
        licznik = 0
        for i in tmp:
            obiekt = i[1]
            zal = obiekt.zaleznosci()
            for j in zal:
                nazwa = 'moduly.' + j
                """pustych nie sprawdzaj"""
                if obiekt.zaleznosci() == '':
                    continue
                try:
                    assert(sys.modules.get(nazwa) != None)
                except AssertionError:
                    wadliwy_modul = str(obiekt).split('.')[1]
                    logging.error(
                                  """[%s] dependency error: \'%s\'.
                                  Module disabled""", wadliwy_modul, j)
                    '''usuń skąd tylko się da'''
                    del(sys.modules['moduly.' + wadliwy_modul])
                    del obiekt
                    del zal
                    self.__zaladowane_obiekty.pop(licznik)
                    self.__zaladowane_pluginy.pop(licznik)
                    menu.usun_pozycje(i[0])
            licznik += 1

    def __sprawdzanie_numeracji(self, menu):
        '''sprawdzanie, czy numeracja w menu nie jest zduplikowana
        i dokonywanie poprawek'''
        pozycje = menu.przekaz_pozycje()
        ost = 0
        do_zamiany = []
        oim = self.__obiekty_i_menu()
        '''dostępna numeracja - od 0 do 10'''
        wolne = range(0, 9 + 1)
        '''tworzenie listy pozycji do zamiany (ale bierze tylko jeden
        z duplikatów'''
        for k, wartosc in pozycje:
            if k == ost:
                do_zamiany.append(wartosc)
                pozycje.pop(pozycje.index((k, wartosc)))
            else:
                wolne.pop(wolne.index(k))
            ost = k
        do_zamiany.sort()

        '''i ich zamiana na pierwszy wolny numer'''
        for wartosc in do_zamiany:
            try:
                numer = wolne.pop(1)
            except IndexError:
                logging.error("[%s] Error: %s",'Moduly','no free space in menu')
                return
            pozycje.append((numer, wartosc))
            self.__zmien_obiekt(oim.get(wartosc), numer)
        pozycje.sort()
        menu.zapisz_pozycje(pozycje)

    def __obiekty_i_menu(self):
        '''podaje słownik pozycji i przypisanych obiektów'''
        obj = {}
        for i in self.__zaladowane_obiekty:
            obiekt = i[1]
            do_menu = obiekt.do_menu()[1]
            obj.update({do_menu:obiekt})
        return obj

    def __zmien_obiekt(self, obiekt, numer):
        '''zmienia numerację na liście obiektów'''
        for i in self.__zaladowane_obiekty:
            if i[1] == obiekt:
                i[0] = numer
                return
