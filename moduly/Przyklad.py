#-*- coding: utf-8 -*-

from moduly.Template import Template
import os

""" UWAGA! nazwa klasy musi być taka sama, jak nazwa pliku """
class Przyklad(Template):
    '''klasa Przyklad'''

    obiekty = {}

    wersja = '1.4'
    info = "Przykladowy moduł"
    pozycja_w_menu = 7
    nazwa_w_menu = 'przykład modułu'

    def __init__(self):
        Template.__init__(self)

    '''----------------- TĄ CZĘŚĆ NALEŻY SKOPIOWAĆ I PRZESŁONIĆ -----------------'''

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''
        os.system("clear")
        print("PRZYKŁAD:")
        print("  0: POWRÓT")

        self.wybor_menu(glowne_menu)

    '''tego nie przysłaniam, bo jest takie samo, ale normalnie trzeba tu dodać własne funkcje'''
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

        '''uzupelnić o własne funkcje'''
        print("\n[Przykład] moja super ekstra funkcja!")
