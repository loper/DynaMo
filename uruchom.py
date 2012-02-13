#-*- coding: utf-8 -*-

"""DynaMo - główny moduł uruchomieniowy
wersja 0.9"""

import getopt
import logging
from sys import argv

import Moduly

OPCJE, ARGUMENTY = getopt.getopt(argv[1:], 'v', 'verbose')

for op, arg in OPCJE:
    if op in ('-v', '--verbose'):
        logging.basicConfig(
                    format='%(message)s (in %(funcName)s at %(lineno)d)',
                    level=logging.DEBUG)
    else:
        logging.basicConfig(
                    format='%(message)s (in %(funcName)s at %(lineno)d)',
                    level=logging.WARNING)

print """DynaMo - główny moduł uruchomieniowy
wersja 0.9"""

MODULY = Moduly.Moduly()
logging.debug("[%s] loaded", 'Moduly')

MENU = MODULY.wczytaj_moduly()
ZALADOWANE = MODULY.podaj_zaladowane()
MENU.przekaz_zaladowane_obiekty(ZALADOWANE)
MENU.pokaz_menu(MODULY)
