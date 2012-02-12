#-*- coding: utf-8 -*-

import os

class Nazwa_modulu:

    __wersja = '0.1'
    __info = "opis"
    __zaleznosci = []

    def __init__(self):
        pass

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def zaleznosci(self):
        return self.__zaleznosci

    def do_menu(self):
        return (5, 'opcja-do-menu')

    def menu(self, zaladowane):
	os.system("clear")
        print "NAZWA_MODULU:"
        print "0. POWRÓT"

        self.__wybor_menu(zaladowane)

    def __wybor_menu(self, zaladowane):
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
                pass
            else:
                print "Błędna opcja"
                continue
        self.menu()
