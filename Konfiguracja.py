#-*- coding: utf-8 -*-
'''umożliwia wczytywanie ustawień do programu'''

class Konfiguracja(object):
    '''klasa Konfiguracja'''
    
    __ustawienia = {}

    def __init__(self, plik):
        self.__otworz_plik(plik)
    
    def __otworz_plik(self, konfig):
        '''otwiera plik i odczytuje z niego konfigurację'''
        plik = open(konfig, 'r')
        plik = plik.readlines()
        for linia in plik:                   
            if len(linia) <= 1:
                continue
            if linia[0] in ('#', '/'):
                continue
            linia = linia.rstrip().split("=")
            if len(linia) != 2:
                continue
            self.__dodaj_do_ustawien(linia[0], linia[1])
            
        
    def __dodaj_do_ustawien(self, klucz, wartosc):
        '''dodaje pozycje do słownika ustawień'''
        self.__ustawienia.update({klucz:wartosc})
        
    def podaj_wartosc(self, klucz):
        try:
            return self.__ustawienia[klucz]
        except:
            return "<brak klucza>"