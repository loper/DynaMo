#-*- coding: utf-8 -*-

"""DynaMo - główny moduł uruchomieniowy"""

import Konfiguracja
import Moduly
import logging
import os


FORMAT = '%(message)s (in %(funcName)s at %(lineno)d)'
logging.basicConfig(format = FORMAT, level = logging.WARNING)

def tryb_verbose():
    '''włącza tryb "gadatliwy"'''
    logging.basicConfig(format = FORMAT, level = logging.DEBUG)

KONF = Konfiguracja.Konfiguracja('ustawienia.cfg')

if KONF.podaj_wartosc("verbose"):
    tryb_verbose()

os.system('clear')
print((KONF.podaj_wartosc("naglowek")))
print(("wersja %s by %s" % (KONF.podaj_wartosc("wersja"),
                           KONF.podaj_wartosc("autor"))))

MODULY = Moduly.Moduly(KONF)
logging.debug("[%s] loaded", 'Moduly')

