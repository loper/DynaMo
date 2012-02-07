#-*- coding: utf-8 -*-
"""pokazuje główne menu"""

import os
import sys

class Menu:

    __pozycje = [(9, 'WYJŚCIE'), (8, 'Moduly')]
    __zaladowane_obiekty = None

    def __init__(self):
        pass

    def pokaz_menu(self, moduly):
        #os.system("clear")
        print "MENU:"
        for i in self.__pozycje:
            print "%d: %s" % (i[0], i[1])
        print "\n"
        self.__wybor_menu(moduly)
        
    def __wybor_menu(self, moduly):
        while(1):
            opcja = input('opcja > ')
            if opcja == 9:
                sys.exit(0)
            elif opcja == 8:
                moduly.menu()
            else:
                print "Błędna opcja"
                continue
            self.pokaz_menu(moduly)


    def dodaj_do_menu(self, element):
        self.__pozycje.append(element)
        self.__pozycje.sort()

    def przekaz_zaladowane_obiekty(self, zaladowane):
        self.__zaladowane_obiekty = zaladowane

