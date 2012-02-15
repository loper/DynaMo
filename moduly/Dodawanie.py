#-*- coding: utf-8 -*-

import os

class Dodawanie:

    __pozycja_w_menu = 1
    __nazwa_w_menu = 'dodaj'
    __wersja = '0.3'
    __info = "Plugin do dodawania liczb calkowitych"
    __zaleznosci = ["Odejmowanie"]

    __liczby = []

    def __init__(self):
        pass

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def zaleznosci(self):
        return self.__zaleznosci

    def do_menu(self):
        '''lista opcji, które idą do menu'''
        return (self.__pozycja_w_menu, self.__nazwa_w_menu)

    def menu(self, glowne_menu, zaladowane):
        os.system("clear")
        print "DODAWANIE:"
        print "1. Wprowadz liczby"
        print "2. Podaj wynik"
        print "3. Solver"
        print "0. POWRÓT"

        self.__wybor_menu(glowne_menu,zaladowane)

    def __wybor_menu(self, glowne_menu,zaladowane):
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                return
            elif opcja == 1:
                self.__liczby = self.__pobierz_liczby()
            elif opcja == 2:
                self.__oblicz_wynik(self.__liczby)
            elif opcja == 3:
                self.__solver(zaladowane)
            else:
                print "Bledna opcja"
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

    def __solver(self, zaladowane):
        #malo eleganckie...
        for k, v in zaladowane:
            if str(v).split('.')[1] == 'Odejmowanie':
                break
        wynik = raw_input('Podaj wynik: ')
        try:
            wynik = int(wynik)
        except Exception:
            print "Błędna liczba"
        odj = raw_input('Podaj odjemną: ')
        try:
            odj = int(odj)
        except Exception:
            print "Błędna liczba"
        print 'Wynik działania: ' + str(v.odejmij([wynik, odj]))
