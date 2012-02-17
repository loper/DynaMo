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

    __pozycje = []
    __zaladowane_obiekty = {}
    __domyslna_opcja = None

    def __init__(self, pokazywac_moduly = True):
        if pokazywac_moduly:
            self.__pozycje = [(8, 'Moduly')]
            self.__zaladowane_obiekty = {8: None}
        else:
            self.__pozycje = []
            self.__zaladowane_obiekty = {}

    def pokaz_menu(self, moduly):
        '''pokazuje pozycje z menu'''
        print(self.formatuj_menu("menu", self.__pozycje))

        '''i pyta o wybór opcji'''
        self.__wybor_menu(moduly)
#        print("MENU:")
#        for i in self.__pozycje:
#            print(("  %d: %s" % (i[0], i[1])))
#        print("  0: WYJŚCIE")


    def formatuj_menu(self, naglowek, pozycje):
        '''formatuje menu do pewnego standardu
        - naglowek jest typu "string" i zostanie 
          zamieniony na duże litery
        - pozycje to lista zawierająca krotki "(nr, "opis")" '''

        '''sprawdzanie formatów'''
        if type(naglowek) != str or type(pozycje) != list:
            logging.error("[%s] Error: %s", 'Menu',
                          'Niewłaściwy format wysłanych danych do formatowania')
            return ''

        '''tworzenie łańcucha, który wystarczy wyświetlić'''
        format_menu = []
        format_menu.append(naglowek.upper() + ":")
        for poz in pozycje:
            format_menu.append("  %d: %s" % (poz[0], poz[1]))
        return "\n".join(format_menu)


    def pytanie_o_opcje(self):
        '''pyta o wybór z menu i zwraca opcję'''
        opcja = eval(input('\nopcja > '))
        try:
            opcja = int(opcja)
        except ValueError:
            return self.__domyslna_opcja
        return opcja

    def __wybor_menu(self, moduly):
        '''wywołuje daną funkcję z menu'''
        while(1):
            opcja = self.pytanie_o_opcje()
            if opcja == None:
                print("Błędna opcja")
                continue
            if opcja == 0:
                os.system("clear")
                sys.exit(0)
            elif opcja == 8:
                moduly.menu(self)
            else:
                try:
                    obj = self.__zaladowane_obiekty[opcja]
                    obj.menu(self)
                except KeyError:
                    print("Błędna opcja")
                    continue
            self.pokaz_menu(moduly)


    def dodaj(self, obiekt, element):
        '''dodaje pozycję do menu, następnie je sortuje'''
        '''najpierw sprawdza duplikaty'''
        numer = element[0]
        if numer in self.__zaladowane_obiekty:
            numer = self.__znajdz_wolny()
            element = (numer, element[1])
        self.__pozycje.append(element)
        self.__pozycje.sort()
        self.__zaladowane_obiekty.update({numer:obiekt})

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
        wolne = list(range(1, 9 + 1))
        for klucz in wolne:
            if klucz not in self.__zaladowane_obiekty:
                return klucz


