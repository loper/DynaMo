#-*- coding: utf-8 -*-
"""pokazuje główne menu

Pozycje w menu są dodawane dynamicznie, oprócz tych, wymienionych w '__pozycje'.
Opcje te odwolują się do funkcji 'menu()' dla danego obiektu
(lista w '__zaladowane_obiekty')."""

import logging
import os
import sys

class Menu:
    '''klasa Menu'''

    __pozycje = [(8, 'Moduly')]
    __zaladowane_obiekty = None

    def __init__(self):
        pass

    def pokaz_menu(self, moduly):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print "MENU:"
        for i in self.__pozycje:
            print "%d: %s" % (i[0], i[1])
        print "0: WYJŚCIE"
        print "\n"
        self.__wybor_menu(moduly)
        
    def __wybor_menu(self, moduly):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = raw_input('opcja > ')
            try:
                opcja = int(opcja)
            except ValueError:
                print "Błędna opcja"
                continue
                
            if opcja == 0:
                os.system("clear")
                sys.exit(0)
            elif opcja == 8:
                moduly.menu()
            else:
                obj = self.__szukaj_modul(opcja)
                if obj == None:
                    print "Błędna opcja"
                    continue
                obj.menu(moduly.podaj_zaladowane())
            self.pokaz_menu(moduly)


    def dodaj_do_menu(self, element):
        '''dodaje pozycję do menu, następnie je sortuje'''
        self.__pozycje.append(element)
        self.__pozycje.sort()

    def przekaz_zaladowane_obiekty(self, zaladowane):
        '''zwraca listę załadowanych obiektów'''
        self.__zaladowane_obiekty = zaladowane

    def przekaz_pozycje(self):
        '''zwraca pozycje z menu'''
        return self.__pozycje

    def zapisz_pozycje(self, pozycje):
        '''zapisuje nową listę pozycji'''
        self.__pozycje = pozycje

    def __szukaj_modul(self, numer):
        '''zwraca obiekt dla podanego numeru'''
        tmp = dict(self.__zaladowane_obiekty)
        try:
            return tmp[numer]
        except KeyError:
            return None

    def usun_pozycje(self, numer):
        '''wyszukuje i usuwa pozycję o podanym numerze z menu'''
        for k, wartosc in self.__pozycje:
            if k == numer:
                logging.debug("[%s] deleting from menu: %s", 'Menu', wartosc)
                self.__pozycje.pop(self.__pozycje.index((k, wartosc)))
        