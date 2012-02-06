import logging

import Menu
import Moduly

#tutaj jakies getopts
#logging.basicConfig(format='%(message)s (in %(funcName)s at %(lineno)d)', level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)

if __name__ == "__main__":
    menu = Menu.Menu()
    logging.debug("[%s] %s loaded", 'program', 'Menu')

    moduly = Moduly.Moduly()
    logging.debug("[%s] %s loaded", 'program', 'Pluginy')

    zaladowane = moduly.wczytaj_moduly(menu)
    menu.przekaz_zaladowane_obiekty(zaladowane)
    menu.pokaz_menu()
