#-*- coding: utf-8 -*-
"""główny moduł uruchomieniowy"""
import logging

import Moduly

#tutaj jakies getopts
logging.basicConfig(format='%(message)s (in %(funcName)s at %(lineno)d)',
                    #    level=logging.DEBUG)
                    level=logging.WARNING)

MODULY = Moduly.Moduly()
logging.debug("[%s] %s loaded", 'program', 'Moduly')

MENU = MODULY.wczytaj_moduly()
ZALADOWANE = MODULY.podaj_zaladowane()
MENU.przekaz_zaladowane_obiekty(ZALADOWANE)
MENU.pokaz_menu(MODULY)
