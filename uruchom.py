#-*- coding: utf-8 -*-
"""główny moduł uruchomieniowy"""
import logging

import Menu
import Moduly

#tutaj jakies getopts
#logging.basicConfig(format='%(message)s (in %(funcName)s at %(lineno)d)',
#    level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
    MENU = Menu.Menu()
    logging.debug("[%s] %s loaded", 'program', 'Menu')

    logging.debug("[%s] %s loaded", 'program', 'Moduly')
    MODULY = Moduly.Moduly()

    ZALADOWANE = MODULY.wczytaj_moduly(MENU)
    MENU.przekaz_zaladowane_obiekty(ZALADOWANE)
    MENU.pokaz_menu(MODULY)
