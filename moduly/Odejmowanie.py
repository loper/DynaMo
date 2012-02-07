class Odejmowanie:
    
    __info = "Plugin do odejmowania liczb calkowitych"
    __wersja = '0.1'
    __zaleznosci = ("Odejmowanie.odejmij")

    def __init__(self):
        pass

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