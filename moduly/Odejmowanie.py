class Odejmowanie:
    
    __info = "Plugin do odejmowania liczb calkowitych"
    __wersja = '0.1'
    __zaleznosci = []

    def __init__(self):
        pass

    def zaleznosci(self):
        return self.__zaleznosci

    def do_menu(self):
        return (2, 'odejmij')

    def info(self):
        return self.__info

    def wersja(self):
        return self.__wersja

    def menu(self):
        pass

    def odejmij(self, liczby):
        wynik = liczby[1]-liczby[0]
        return wynik