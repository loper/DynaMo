#-*- coding: utf-8 -*-
"""pusty moduł, który należy wypełnić według uznania

Stanowi wzorzec dla nowych modułów, ładowanych z poziomu 'Moduly.py'

Obowiązkowe funkcje:
    - info()
    - wersja()
    - zaleznosci()
    - zapisz_obiekty()

Obowiązkowe pola:
    - wersja
    - info
    
Jeżeli moduł ma dodawać swoją opcję do menu, obowiązkowe są:
    - __do_menu()
    - pozycja_w_menu
    - nazwa_w_menu

Dostęp do konfiguracji jest z poziomu self.obiekty['konfiguracja'],
a odczyt wartości przy pomocy funkcji 'podaj_wartosc(klucz)'.
"""

import os

""" UWAGA! nazwa klasy musi być taka sama, jak nazwa pliku """
class Template:
    '''klasa Template'''

    '''----------------- SKOPIOWAĆ I USTAWIĆ WEDŁUG UZNANIA -----------------'''
    wersja = '0.1'

    '''opis max. 40 znaków'''
    info = "opis"

    '''jeżeli program dodaje opcję do menu'''
    pozycja_w_menu = 5
    nazwa_w_menu = 'nazwa w menu'

    ''' dla pustych zależności ustawić "[]" lub nie umieszczać zmiennej;
     pamiętać o "moduly." 
     np. zaleznosci = ['moduly.NiezbednyModul', 'moduly.InnyWaznyModul']'''
    zaleznosci = []

    '''nie zmieniać, ale skopiować'''
    obiekty = {}

    '''----------------- NIE ZMIENIAĆ -----------------'''


    def __init__(self):
        self.obiekty = {}

    def podaj_info(self):
        '''zwraca opis modułu'''
        return self.info

    def podaj_wersje(self):
        '''zwraca wersję modułu'''
        return self.wersja

    def podaj_zaleznosci(self):
        '''zwraca listę zależności'''
        try:
            return self.zaleznosci
        except AttributeError:
            return []

    def do_menu(self):
        '''wysłanie listy opcji, które idą do menu'''
        if 'menu' in self.obiekty:
            self.obiekty['menu'].dodaj(self, (self.pozycja_w_menu,
                                              self.nazwa_w_menu))

    def zapisz_obiekty(self, obiekty):
        '''zapis przekazanych obiektów'''
        self.obiekty = obiekty

        '''uruchomienie modułu'''
        self.uruchom_modul()

    '''----------- TĄ CZĘŚĆ NALEŻY SKOPIOWAĆ I PRZESŁONIĆ -----------'''

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''

        '''pusty słownik pozycji'''
        pozycje = []
        '''do którego dodajemy krotki (nr, 'opis')'''
        pozycje.append((0, 'POWRÓT'))
        '''i wywołanie menu.formatuj_menu(nagłowek, pozycje)'''
        self.obiekty['menu'].formatuj_menu('przyklad', pozycje)

        self.wybor_menu(glowne_menu)

    def wybor_menu(self, glowne_menu):
        '''pyta o wybór i wywołuje daną funkcję'''
        while(1):
            opcja = glowne_menu.pytanie_o_opcje()
            if opcja == 0:
                os.system('clear')
                return
            elif opcja == 1:
                pass
            else:
                print("Błędna opcja")
                continue
        self.menu(glowne_menu)

    def uruchom_modul(self):
        '''dodanie pozycji do menu'''
        '''tą część można skasować, jeśli ma nie być dodawana pozycja do menu'''
        self.do_menu()

        '''uzupelnić o własne funkcje'''
