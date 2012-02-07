#-*- coding: utf-8 -*-
class Dodawanie:

    __wersja = '0.1'

    def __init__(self):
        pass

    def do_menu(self):
        return (1, 'dodaj')

    def info(self):
        print "Plugin do dodawania liczb calkowitych"

    def wersja(self):
        return self.__wersja

    def menu(self):
        # os.system("clear")
        print "DODAWANIE:"
        print "1. Wprowadz liczby"
        print "2. Podaj wynik"
        print "3. Solver"
        print "0. POWRÓT"

        self.__wybor_menu()

    def __wybor_menu(self):
        while(1):
            opcja = input('opcja > ')
            if opcja == 0:
                return
            elif opcja == 1:
                self.__wypisz_zaladowane()
            elif opcja == 2:
                self.wczytaj_moduly()
                #TODO: menu nie jest przekazywane do uruchom.py
                print "Moduły zostały przeładowane"
            else:
                print "Bledna opcja"
                continue
            self.menu()