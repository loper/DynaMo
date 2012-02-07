#-*- coding: utf-8 -*-
class Dodawanie:

    __wersja = '0.1'
    __info = "Plugin do dodawania liczb calkowitych"

    def __init__(self):
        pass

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def do_menu(self):
        return (1, 'dodaj')

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
                pass
            elif opcja == 2:
                pass
            else:
                print "Bledna opcja"
                continue
            self.menu()

    def __pobierz_liczby(self):
        liczba1=