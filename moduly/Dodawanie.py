class Dodawanie:

    __wersja='0.1'

    def __init__(self):
        pass

    def do_menu(self):
        return (1,'dodaj')

    def info(self):
        print "Plugin do dodawania liczb calkowitych"

    def wersja(self):
        return self.__wersja