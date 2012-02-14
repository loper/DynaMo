#-*- coding: utf-8 -*-
'''umożliwia wczytywanie ustawień do programu'''

class Konfiguracja(object):
    '''klasa Konfiguracja'''

    def __init__(self, plik):
        self.__otworz_plik(plik)
    
    def __otworz_plik(self, konfig):
        plik = open(konfig, 'r')
        plik = plik.readlines()
        for linia in plik:                   
            if len(linia) <= 1:
                continue
            if linia[0] in ('#', '/'):
                continue
            linia=linia.rstrip()
            