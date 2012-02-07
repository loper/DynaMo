#-*- coding: utf-8 -*-
class Dodawanie:

    __wersja = '0.1'
    __info = "Plugin do dodawania liczb calkowitych"
    __zaleznosci = ["Odejmowanie","All"]

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
        return (1, 'dodaj')

    def menu(self):
        # os.system("clear")
        print "DODAWANIE:"
        print "1. Wprowadz liczby"
        print "2. Podaj wynik"
        print "3. Solver"
        print "0. POWRÓT"

        #to nie moze tu byc
        self.__wybor_menu()

    def __wybor_menu(self):
        while(1):
            opcja = input('opcja > ')
            if opcja == 0:
                return
            elif opcja == 1:
                self.__liczby = self.__pobierz_liczby()
            elif opcja == 2:
                self.__oblicz_wynik(self.__liczby)
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
