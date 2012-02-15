#-*- coding: utf-8 -*-

import os

class Dodawanie:

    __pozycja_w_menu = 1
    __nazwa_w_menu = 'dodaj'
    __wersja = '0.6'
    __info = "Plugin do dodawania liczb calkowitych"
    __zaleznosci = []

    __liczby = []
    __obiekty = {}

    def __init__(self):
        pass

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def zaleznosci(self):
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
        os.system("clear")
        print "DODAWANIE:"
        print "1. Wprowadz liczby"
        print "2. Podaj wynik"
        print "3. Solver"
        print "0. POWRÓT"

        self.__wybor_menu(glowne_menu)

    def __wybor_menu(self, glowne_menu):
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                return
            elif opcja == 1:
                self.__liczby = self.__pobierz_liczby()
            elif opcja == 2:
                self.__oblicz_wynik(self.__liczby)
#            elif opcja == 3:
#                self.__solver()
            else:
                print "Błędna opcja"
                continue
        self.menu()

    def __pobierz_liczby(self):
        liczby = []
        for i in range(1, 3):
            liczba = raw_input('Podaj liczbę nr %d: ' % i)
            try:
                liczba = int(liczba)
            except Exception:
                print "Błędna liczba"
                self.__pobierz_liczby()
            liczby.append(liczba)
        print "Liczby %s zostały zapisane w pamięci" % liczby
        return liczby

    def __oblicz_wynik(self, liczby):
        if liczby == []:
            print "Nie wprowadzono liczb"
            return
        wynik = self.dodaj(liczby)
        print "Wynik działania: %d" % wynik

    def dodaj(self, liczby):
        wynik = liczby[0] + liczby[1]
        return wynik

#    def __solver(self):
#        #malo eleganckie...
#        for k, v in zaladowane:
#            if str(v).split('.')[1] == 'Odejmowanie':
#                break
#        wynik = raw_input('Podaj wynik: ')
#        try:
#            wynik = int(wynik)
#        except Exception:
#            print "Błędna liczba"
#        odj = raw_input('Podaj odjemną: ')
#        try:
#            odj = int(odj)
#        except Exception:
#            print "Błędna liczba"
#        print 'Wynik działania: ' + str(v.odejmij([wynik, odj]))
