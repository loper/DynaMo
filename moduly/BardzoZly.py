#-*- coding: utf-8 -*-
from moduly._Wzor import _Wzor

#TODO: za długa nazwa modułu?
#tak się chyba nie da, bo system ogranicza długość nazw plików
#class BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_BardzoZly_(Wzor):
class BardzoZly(_Wzor):

    obiekty = {}
    wersja = 'xX'
    info = 'bbbb'
    pozycja_w_menu = 9
    nazwa_w_menu = 'aaaa'
    zaleznosci = []

    def __init__(self):
        super().__init__()

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''

        '''pusty słownik pozycji'''
        pozycje = []
        '''do którego dodajemy krotki (nr, 'opis')'''
        pozycje.append((0, 222))

        '''i wywołanie menu.formatuj_menu(nagłowek, pozycje)'''
        naglowek = "Bardzo, bardzo zly"
        self.obiekty['menu'].formatuj_menu(naglowek, pozycje)

        self.wybor_menu(glowne_menu)

#    def wybor_menu(self, glowne_menu):
#        '''pyta o wybór i wywołuje daną funkcję'''
#        while(1):
#            opcja = glowne_menu.pytanie_o_opcje()
#            if opcja == 0:
#                os.system('clear')
#                return
#            else:
#                print "Błędna opcja"
#                continue
#        self.menu()

    def uruchom_modul(self):
        '''dodanie pozycji do menu'''
        '''tą część można skasować, jeśli ma nie być dodawana pozycja do menu'''
        self.do_menu()

