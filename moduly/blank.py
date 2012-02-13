#-*- coding: utf-8 -*-
"""pusty moduł, który należy wypełnić według uznania

Stanowi wzorzec dla nowych modułów, ładowanych z poziomu 'Moduły.py'

Obowiązkowe funkcje:
    - info()
    - wersja()
    - zaleznosci()
    - do_menu()
    - menu()

Obowiązkowe pola:
    - __wersja
    - __info
    - __pozycja_w_menu
    - __nazwa_w_menu
    - __zależności
"""

import os

class Nazwamodulu:
    'klasa Nazwamodulu'

    __wersja = '0.1'
    __info = "opis"
    __pozycja_w_menu = 5
    __nazwa_w_menu = 'nazwa w menu'
    __zaleznosci = ['NiezbednyModul', 'InnyWaznyModul']
    '''dla pustych zależności ustawić "[]"'''

    def __init__(self):
        pass

    def info(self):
        '''zwraca opis modułu'''
        return self.__info

    def wersja(self):
        '''zwraca wersję modułu'''
        return self.__wersja

    def zaleznosci(self):
        '''zwraca listę zależności'''
        return self.__zaleznosci

    def do_menu(self):
        '''lista opcji, które idą do menu'''
        return (self.__pozycja_w_menu, self.__nazwa_w_menu)

    def menu(self, glowne_menu, zaladowane):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print "NAZWA_MODULU:"
        print "  1: lista przekazanych obiektów"
        print "  0: POWRÓT"

        self.__wybor_menu(glowne_menu)

    def __wybor_menu(self, glowne_menu, zaladowane):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                return
            elif opcja == 1:
                print zaladowane
            else:
                print "Błędna opcja"
                continue
        self.menu()
