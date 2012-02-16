#-*- coding: utf-8 -*-

"""DynaMo - główny moduł uruchomieniowy"""

import getopt
import logging
import os
from sys import argv

import Moduly
import Konfiguracja

FORMAT = '%(message)s (in %(funcName)s at %(lineno)d)'

def tryb_verbose(wlaczyc = False):
    '''włącza tryb "gadatliwy"'''
    if wlaczyc:
        logging.basicConfig(format = FORMAT, level = logging.DEBUG)
    else:
        logging.basicConfig(format = FORMAT, level = logging.WARNING)

KONF = Konfiguracja.Konfiguracja('ustawienia.cfg')

''' dwa sposoby włączania trybu gadatliwego:
albo konfiguracja albo przełącznik'''
if KONF.podaj_wartosc("verbose"):
    tryb_verbose(True)

OPCJE, ARGUMENTY = getopt.getopt(argv[1:], 'v', 'verbose')

for op, arg in OPCJE:
    if op in ('-v', '--verbose'):
        tryb_verbose(True)

os.system('clear')
print(KONF.podaj_wartosc("naglowek"))
print("wersja %s by %s" % (KONF.podaj_wartosc("wersja"),
                           KONF.podaj_wartosc("autor")))

MODULY = Moduly.Moduly(KONF)
logging.debug("[%s] loaded", 'Moduly')

