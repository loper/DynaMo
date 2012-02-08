class Odejmowanie:
    
    __info = "Plugin do odejmowania liczb calkowitych"
    __wersja = '0.1'
    __zaleznosci = []

    def __init__(self):
        pass

    def zaleznosci(self):
        return self.__zaleznosci

    def do_menu(self):
        return (1, 'odejmij')

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def menu(self):
        print "odejmowanie menu..."

    def odejmij(self, liczby):
        wynik = liczby[0]-liczby[1]
        return wynik