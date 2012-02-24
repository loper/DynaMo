#-*- coding: utf-8 -*-

""" Przykładowy moduł, który należy traktować jako wzór i skasować po napisaniu
własnego """
from moduly._Wzor import _Wzor

""" UWAGA! nazwa klasy musi być taka sama, jak nazwa pliku """
class Przyklad(_Wzor):
    '''klasa Przyklad'''

    obiekty = {}

    wersja = '1.7'
    info = "Przykladowy moduł"
    pozycja_w_menu = 7
    nazwa_w_menu = 'przykład modułu'
    zaleznosci = []

    def __init__(self):
        super().__init__()

    '''----------- TĄ CZĘŚĆ NALEŻY SKOPIOWAĆ I PRZESŁONIĆ -----------'''

    '''tego nie przysłaniam, bo jest takie samo, ale normalnie trzeba tu dodać 
       własne funkcje'''

#    def menu(self, glowne_menu):
#        '''pokazuje pozycje z menu'''
#
#        '''pusty słownik pozycji'''
#        pozycje = []
#        '''do którego dodajemy krotki (nr, 'opis')'''
#        pozycje.append((0, 'POWRÓT'))
#        naglowek = 'przyklad'
#        '''i wywołanie menu.formatuj_menu(nagłowek, pozycje)'''
#        self.obiekty['menu'].formatuj_menu(naglowek, pozycje)
#
#        self.wybor_menu(glowne_menu)

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

        '''uzupelnić o własne funkcje uruchomione po zaladowaniu'''
        #print("\n[Przykład] moja super ekstra funkcja!")
