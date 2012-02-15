#-*- coding: utf-8 -*-

"""DynaMo - główny moduł uruchomieniowy"""

import getopt
import logging
import os
from sys import argv

import Moduly
import Konfiguracja

def tryb_verbose(wlaczyc = False):
    '''włącza tryb "gadatliwy"'''
    if wlaczyc:
        logging.basicConfig(level = logging.DEBUG)
    else:
        logging.basicConfig(level = logging.WARNING)

logging.basicConfig(format = '%(message)s (in %(funcName)s at %(lineno)d)')

KONF = Konfiguracja.Konfiguracja('ustawienia.cfg')

''' dwa sposoby włączania trybu gadatliwego:
albo konfiguracja albo przełącznik'''
if KONF.podaj_wartosc("verbose") == 'y':
    tryb_verbose(True)
else:
    OPCJE, ARGUMENTY = getopt.getopt(argv[1:], 'v', 'verbose')

    for op, arg in OPCJE:
        if op in ('-v', '--verbose'):
            tryb_verbose(True)
        else:
            tryb_verbose(False)

os.system('clear')
#print 20 * "\n"
print KONF.podaj_wartosc("naglowek")
print "wersja %s by %s" % (KONF.podaj_wartosc("wersja"),
                           KONF.podaj_wartosc("autor"))

MODULY = Moduly.Moduly(KONF)
logging.debug("[%s] loaded", 'Moduly')

