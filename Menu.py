#-*- coding: utf-8 -*-
"""pokazuje główne menu"""

import logging
import sys

class Menu:

    __pozycje = [(8, 'Moduly')]
    __zaladowane_obiekty = None

    def __init__(self):
        pass

    def pokaz_menu(self, moduly):
        #os.system("clear")
        print "MENU:"
        for i in self.__pozycje:
            print "%d: %s" % (i[0], i[1])
        print "0: WYJŚCIE"
        print "\n"
        self.__wybor_menu(moduly)
        
    def __wybor_menu(self, moduly):
        while(1):
            opcja = raw_input('opcja > ')
            try:
                opcja = int(opcja)
            except Exception:
                print "Błędna opcja"
                continue
                
            if opcja == 0:
                sys.exit(0)
            elif opcja == 8:
                moduly.menu()
            else:
                obj = self.__szukaj_modul(opcja)
                if obj == None:
                    print "Błędna opcja"
                    continue
                obj.menu(moduly.podaj_zaladowane())
            self.pokaz_menu(moduly)


    def dodaj_do_menu(self, element):
        self.__pozycje.append(element)
        self.__pozycje.sort()

    def przekaz_zaladowane_obiekty(self, zaladowane):
        self.__zaladowane_obiekty = zaladowane

    def przekaz_pozycje(self):
        return self.__pozycje

    def __szukaj_modul(self, numer):
        tmp = dict(self.__zaladowane_obiekty)
        try:
            return tmp[numer]
        except KeyError:
            return None

    def usun_pozycje(self, nr):
        for k, v in self.__pozycje:
            if k == nr:
                logging.debug("[%s] deleting from menu: %s", 'Menu', v)
                self.__pozycje.pop(self.__pozycje.index((k, v)))
        
        

#TODO: testy, czy moduly poprawnie sie wczytuja