#-*- coding: utf-8 -*-

from moduly.Template import Template

class BardzoZly(Template):

    obiekty = {}
    wersja = 'aa'
    info = 'None'
    pozycja_w_menu = 999
    nazwa_w_menu = 'aaaa'
    zaleznosci = []

    def __init__(self):
        super().__init__()
#        for i in range(1, 500):
#            self.zaleznosci.append(str(i))

    '''----------- TĄ CZĘŚĆ NALEŻY SKOPIOWAĆ I PRZESŁONIĆ -----------'''

    '''tego nie przysłaniam, bo jest takie samo, ale normalnie trzeba tu dodać 
       własne funkcje'''

    def menu(self, glowne_menu):
        '''pokazuje pozycje z menu'''

        '''pusty słownik pozycji'''
        pozycje = []
        '''do którego dodajemy krotki (nr, 'opis')'''
        pozycje.append((0, 222))
        #for i in range(1, 100):
            #pozycje.append((i, 'dupl'))
        '''i wywołanie menu.formatuj_menu(nagłowek, pozycje)'''
        naglowek = "Bardzo, bardzo zly"
        #TODO: sprawdzenie tego
#        naglowek *= 500
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

