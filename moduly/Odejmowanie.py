class Odejmowanie:
    
    __wersja = '0.1'

    def __init__(self):
        pass

    def do_menu(self):
        return (2, 'odejmij')

    def info(self):
        print "Plugin do odejmowania liczb calkowitych"
        print self.__wersja

    def wersja(self):
        return self.__wersja

    def menu(self):
        pass

    def odejmij(self, liczby):
        wynik = liczby[1]-liczby[0]
        return wynik