#-*- coding: utf-8 -*-
'''umożliwia wczytywanie ustawień do programu'''
import logging

class Konfiguracja:
    '''klasa Konfiguracja'''

    __ustawienia = {}

    def __init__(self, plik):
        self.__otworz_plik(plik)

    def __otworz_plik(self, konfig):
        '''otwiera plik i odczytuje z niego konfigurację'''
        try:
            plik_konf = open(konfig, 'r')
            for linia in plik_konf.readlines():
                if len(linia) <= 1:
                    continue
                if linia[0] in ('#', '/'):
                    continue
                linia = linia.rstrip().split("=")
                if len(linia) != 2:
                    continue
                if linia[1] in ('t'):
                    linia[1] = True
                elif linia[1] in ('n'):
                    linia[1] = False
                self.__dodaj_do_ustawien(linia[0], linia[1])
            del plik_konf
        except IOError:
            logging.error(
            "Błąd: Nie można odnaleźć pliku konfiguracyjnego '%s'",
                          konfig)
            exit(-1)


    def __dodaj_do_ustawien(self, klucz, wartosc):
        '''dodaje pozycje do słownika ustawień'''
        self.__ustawienia.update({klucz:wartosc})

    def podaj_wartosc(self, klucz):
        '''zwraca wartość ze słownika __ustawienia dla podanego klucza '''
        try:
            return self.__ustawienia[klucz]
        except KeyError:
            return "<brak klucza>"
