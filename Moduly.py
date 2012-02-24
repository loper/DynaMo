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
        logging.debug("[{}] loaded".format('Menu'))

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

        #tego nie, bo jak dziedziczy, to nie musi sprawdzać

#        '''czy wszystkie funkcje są?'''
#        obowiazkowe = ('podaj_zaleznosci', 'podaj_info', 'podaj_wersje',
#                     'zapisz_obiekty')
#        obowiazkowe = ('zapisz_obiekty')
#        try:
#            for atrybut in obowiazkowe:
#                if not hasattr(obiekt, atrybut):
#                    return False
#        except AttributeError:
#            return False

        '''sprawdzanie zgodności typów atrybutów'''
        if not isinstance(obiekt.info, str):
            return False
        if not isinstance(obiekt.wersja, str):
            return False
        if not isinstance(obiekt.pozycja_w_menu, int):
            return False
        if not obiekt.pozycja_w_menu in range(1, 10):
            return False

        '''obcinanie do ustalonej długości'''
        obiekt.info = obiekt.info[:40]
        obiekt.wersja = obiekt.wersja[:10]
        obiekt.nazwa_w_menu = obiekt.nazwa_w_menu[:20]

        return True


    def __wczytaj_moduly(self):
        '''dynamiczne wczytywanie i szukanie pluginow w folderze "moduly"'''
        lista_plikow = os.listdir('moduly')
        pliki_py = re.compile("\.py$")
        znalezione = [k for k in lista_plikow if pliki_py.search(k)]
        nazwa_na_modul = lambda f: os.path.splitext(f)[0]
        for k in znalezione:
            i = nazwa_na_modul(k)
            """wszystko, oprócz __init__ i_Wzor"""
            if i in('__init__', '_Wzor'):
                continue

            """pluginy"""
            mod = __import__('moduly.{}'.format(i))
            """modul"""
            mod = getattr(mod, i)
            nazwa = mod.__name__
            """obiekt"""
            try:
                mod = getattr(mod, i)
            except AttributeError as err:
                logging.error("[{}] Error: {}".format(i, err))
                continue
            obiekt = mod()
            if not self.__sprawdz_poprawnosc(obiekt):
                del sys.modules[nazwa]
                logging.error("[{}] Error: module is incorrect".format(i))
                continue

            self.__zaladowane_obiekty.update({nazwa: obiekt})
            nazwa = nazwa + " (ver. {})\n     : {}".format(
                obiekt.wersja, obiekt.info[:40 - 1])
            self.__zaladowane_pluginy.append(nazwa)
            logging.debug("[{}] plugin loaded".format(i))


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
        pozycje = []
        pozycje.append((1, 'Lista modułów'))
        pozycje.append((0, 'POWRÓT'))

        self.__obiekty['menu'].formatuj_menu('moduły', pozycje)

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
            zal = obiekt.zaleznosci

            '''sprawdź liczebność zależności'''
            blad = False
            if len(zal) > 10:
                blad = True

            for zaleznosc in zal:
                """pustych nie sprawdzaj"""
                if zaleznosc == '':
                    continue

                '''obetnij długość każdej do zakresu'''
                zaleznosc = zaleznosc[:20]

                if sys.modules.get(zaleznosc) == None or blad:
                    wadliwy_modul = str(obiekt).split('.')[1]
                    logging.error(
                    """[{}] dependency failure: \'{}\'. Module disabled""".
                    format(wadliwy_modul, zaleznosc))

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
                    break

    def __przekaz_obiekty(self, obiekty, zaladowane):
        '''tworzy pakiet i przekazuje go do wszystkich obiektow'''
        do_przekazania = {}
        do_przekazania.update(obiekty)
        do_przekazania.update(zaladowane)
        for obiekt in zaladowane:
            zaladowane[obiekt].zapisz_obiekty(do_przekazania)
