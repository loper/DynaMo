#-*- coding: utf-8 -*-
"""pusty moduł, który należy wypełnić według uznania

Stanowi wzorzec dla nowych modułów, ładowanych z poziomu 'Moduly.py'

Obowiązkowe funkcje:
    - info()
    - wersja()
    - zaleznosci()
    - zapisz_obiekty()

Obowiązkowe pola:
    - __wersja
    - __info
    - __zaleznosci
    
Jeżeli moduł ma dodawać swoją opcję do menu, obowiązkowe są:
    - __do_menu()
    - __pozycja_w_menu
    - __nazwa_w_menu

Dostęp do konfiguracji jest z poziomu self.__obiekty['konfiguracja'],
a odczyt wartości przy pomocy funkcji 'podaj_wartosc(klucz)'.
"""

import os

class Nazwamodulu:
    'klasa Nazwamodulu'

    __wersja = '0.1'
    __info = "opis"
    __pozycja_w_menu = 5
    __nazwa_w_menu = 'nazwa w menu'
    __zaleznosci = ['moduly.NiezbednyModul', 'moduly.InnyWaznyModul']
    '''dla pustych zależności ustawić "[]"'''

    __obiekty = {}

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

    def __do_menu(self):
        '''wysłanie listy opcji, które idą do menu'''
        if self.__obiekty.has_key('menu'):
            self.__obiekty['menu'].dodaj(self, (self.__pozycja_w_menu, self.__nazwa_w_menu))

    def zapisz_obiekty(self, obiekty):
        '''zapis przekazanych obiektów'''
        self.__obiekty = obiekty

        '''dodanie pozycji do menu'''
        self.__do_menu()

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print "NAZWA_MODULU:"
        print "  0: POWRÓT"

        self.__wybor_menu(glowne_menu)

    def __wybor_menu(self, glowne_menu):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                return
            elif opcja == 1:
                pass
            else:
                print "Błędna opcja"
                continue
        self.menu()
