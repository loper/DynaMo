#-*- coding: utf-8 -*-

"""wyszukuje i dynamicznie wczytuje moduły i tworzy ich obiekty

Modułów szuka w 'moduly/'. Wczytuje je i tworzy listę obiektów, które są
wywoływane z poziomu menu. Dodatkowo wypisuje ich listę."""

import Menu
import copy
import logging
import os
import re
import sys


class Moduly:
    '''klasa Moduly'''

    __zaladowane_obiekty = {}
    __zaladowane_pluginy = []

    __obiekty = {}

    def __init__(self, konfiguracja):
        '''zapisz obiekt konfiguracji'''
        self.__obiekty.update({'konfiguracja': konfiguracja})

        '''stwórz menu'''
        menu = Menu.Menu(konfiguracja.podaj_wartosc("moduly_w_menu"))
        self.__obiekty.update({'menu': menu})
        logging.debug("[%s] loaded", 'Menu')

        '''wczytaj moduły'''
        self.__wczytaj_moduly()

        '''sprawdź zależności między modułami'''
        self.__sprawdz_zaleznosci(self.__zaladowane_obiekty)

        '''przekaż obiekty do modułów'''
        self.__przekaz_obiekty(self.__obiekty, self.__zaladowane_obiekty)

        '''pokaż menu'''
        self.__obiekty['menu'].pokaz_menu(self)


    def __sprawdz_poprawnosc(self, obiekt):
        """sprawdzanie poprawności modułu"""
        obowiazkowe = ('podaj_zaleznosci', 'podaj_info', 'podaj_wersje',
                     'zapisz_obiekty')
        try:
            for atrybut in obowiazkowe:
                if not hasattr(obiekt, atrybut):
                    return False
        except AttributeError:
            return False
        return True


    def __wczytaj_moduly(self):
        '''dynamiczne wczytywanie i szukanie pluginow w folderze "moduly"'''
        lista_plikow = os.listdir('moduly')
        pliki_py = re.compile("\.py$")
        znalezione = [k for k in lista_plikow if pliki_py.search(k)]
        nazwa_na_modul = lambda f: os.path.splitext(f)[0]

        for k in znalezione:
            i = nazwa_na_modul(k)
            """wszystko, oprócz __init__ i Template"""
            if i in('__init__', 'Template'):
                continue

            """pluginy"""
            mod = __import__('moduly.%s' % i)
            """modul"""
            mod = getattr(mod, i)
            nazwa = mod.__name__
            """obiekt"""
            try:
                mod = getattr(mod, i)
            except AttributeError as err:
                logging.error("[%s] Error: %s", i, err)
                continue
            obiekt = mod()
            if not self.__sprawdz_poprawnosc(obiekt):
                del sys.modules[nazwa]
                logging.error("[%s] Error: module is incorrect", i)
                continue

            self.__zaladowane_obiekty.update({nazwa: obiekt})
            nazwa = nazwa + " (ver. %s)\n     : %s" % (obiekt.podaj_wersje(),
                                            obiekt.podaj_info()[:40 - 1])
            self.__zaladowane_pluginy.append(nazwa)
            logging.debug("[%s] plugin loaded", i)


    def podaj_zaladowane(self):
        '''zwraca listę załadowanych'''
        return self.__zaladowane_obiekty

    def __wypisz_zaladowane(self):
        '''wypisuje listę załadowanych i ich wersje'''
        if self.__zaladowane_pluginy == []:
            print("brak załadowanych modułów")
        else:
            print("\nZAŁADOWANE MODUŁY:")
            for i in self.__zaladowane_pluginy:
                print(('   - ' + i))

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print("MODUŁY:")
        print("  1. Lista modułów")
        print("  0. POWRÓT")

        self.__wybor_menu(glowne_menu)

    def __wybor_menu(self, glowne_menu):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                os.system('clear')
                return
            elif opcja == 1:
                self.__wypisz_zaladowane()
            else:
                print("Błędna opcja")
                continue
        self.menu(glowne_menu)

    def __sprawdz_zaleznosci(self, obiekty):
        '''sprawdza, czy spełnione są zależności między modułami
        i ewentualnie wyłącza "złe" moduły'''
        for i in copy.copy(obiekty):
            obiekt = obiekty[i]
            zal = obiekt.podaj_zaleznosci()
            for zaleznosc in zal:
                """pustych nie sprawdzaj"""
                if zaleznosc == '':
                    continue
                if sys.modules.get(zaleznosc) == None:
                    wadliwy_modul = str(obiekt).split('.')[1]
                    logging.error(
                    """[%s] dependency failure: \'%s\'. Module disabled""",
                    wadliwy_modul, zaleznosc)

                    '''usuń skąd tylko się da'''
                    del(sys.modules['moduly.' + wadliwy_modul])
                    del obiekt
                    del zal
                    self.__zaladowane_obiekty.pop(i)
                    for j in copy.copy(self.__zaladowane_pluginy):
                        if j.find(i) >= 0:
                            self.__zaladowane_pluginy.pop(
                                            self.__zaladowane_pluginy.index(j))
                            break

    def __przekaz_obiekty(self, obiekty, zaladowane):
        '''tworzy pakiet i przekazuje go do wszystkich obiektow'''
        do_przekazania = {}
        do_przekazania.update(obiekty)
        do_przekazania.update(zaladowane)
        for obiekt in zaladowane:
            zaladowane[obiekt].zapisz_obiekty(do_przekazania)
