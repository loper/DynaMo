#-*- coding: utf-8 -*-
"""pokazuje główne menu

Pozycje w menu są dodawane dynamicznie, oprócz tych, wymienionych w '__pozycje'.
Opcje te odwolują się do funkcji 'menu()' dla danego obiektu
(lista w '__zaladowane_obiekty')."""

import logging
#import os
import sys

class Menu:
    '''klasa Menu'''

    __pozycje = []
    __zaladowane_obiekty = {}

    def __init__(self, pokazywac_moduly = True):
        if pokazywac_moduly:
            self.__pozycje = [(8, 'Moduly')]
            self.__zaladowane_obiekty = {8: None}
        else:
            self.__pozycje = []
            self.__zaladowane_obiekty = {}

    def pokaz_menu(self, moduly):
        '''pokazuje pozycje z menu'''
        print "\nMENU:"
        for i in self.__pozycje:
            print "  %d: %s" % (i[0], i[1])
        print "  0: WYJŚCIE"
        self.__wybor_menu(moduly)

    def pytanie_o_opcje(self):
        '''pyta o wybór z menu i zwraca opcję'''
        opcja = raw_input('\nopcja > ')
        try:
            opcja = int(opcja)
        except ValueError:
            return None
        return opcja

    def __wybor_menu(self, moduly):
        '''wywołuje daną funkcję z menu'''
        while(1):
            opcja = self.pytanie_o_opcje()
            if opcja == None:
                print "Błędna opcja"
                continue
            if opcja == 0:
                #os.system("clear")
                print 20 * "\n"
                sys.exit(0)
            elif opcja == 8:
                moduly.menu(self)
            else:
                obj = self.__zaladowane_obiekty[opcja]
                obj.menu(self)
            self.pokaz_menu(moduly)


    def dodaj(self, obiekt, element):
        '''dodaje pozycję do menu, następnie je sortuje'''
        '''najpierw sprawdza duplikaty'''
        nr = element[0]
        if self.__zaladowane_obiekty.has_key(nr):
            nr = self.__znajdz_wolny()
            element = (nr, element[1])
        self.__pozycje.append(element)
        self.__pozycje.sort()
        self.__zaladowane_obiekty.update({nr:obiekt})

    def przekaz_zaladowane_obiekty(self, zaladowane):
        '''zwraca listę załadowanych obiektów'''
        self.__zaladowane_obiekty = zaladowane

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

    def __znajdz_wolny(self):
        '''dostępna numeracja - od 1 do 10'''
        wolne = range(1, 9 + 1)
        for klucz in wolne:
            if not self.__zaladowane_obiekty.has_key(klucz):
                return klucz


