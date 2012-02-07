class Odejmowanie:
    
    __wersja='0.1'

    def __init__(self):
        pass

    def do_menu(self):
        return (2,'odejmij')

    def info(self):
        print "Plugin do odejmowania liczb calkowitych"
        print self.__wersja

    def wersja(self):
        return self.__wersja