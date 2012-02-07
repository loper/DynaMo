#-*- coding: utf-8 -*-
"""główny moduł uruchomieniowy"""
import logging

import Moduly

#tutaj jakies getopts
#logging.basicConfig(format='%(message)s (in %(funcName)s at %(lineno)d)',
#    level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)

logging.debug("[%s] %s loaded", 'program', 'Moduly')
MODULY = Moduly.Moduly()

MENU = MODULY.wczytaj_moduly()
ZALADOWANE = MODULY.podaj_zaladowane()
MENU.przekaz_zaladowane_obiekty(ZALADOWANE)
MENU.pokaz_menu(MODULY)
