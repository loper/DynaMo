#-*- coding: utf-8 -*-

import os

class Moja:

    __wersja = '0.9'
    __info = "testy"
    __zaleznosci = ["Dodawanie","xOdejmowanie"]

    def __init__(self):
        pass

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def zaleznosci(self):
        return self.__zaleznosci

    def do_menu(self):
        return (6, 'test')

    def menu(self, zaladowane):
	os.system("clear")
        print "MOJA:"
        print "0. POWRÓT"

        self.__wybor_menu(zaladowane)

    def __wybor_menu(self, zaladowane):
        while(1):
            opcja = raw_input('opcja > ')
            try:
                opcja = int(opcja)
            except Exception:
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
