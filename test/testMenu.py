'''
Created on 18-02-2012

@author: loper
'''
import sys
import unittest


class Test(unittest.TestCase):

    __menu = None

    def setUp(self):
        import Menu
        self.__menu = Menu.Menu()


    def tearDown(self):
        del self.__menu


    def test_formatuj_menu(self):
        naglowek = "test"
        pozycje = [(1, 'a'), (2, 'b')]
        wynik = self.__menu.formatuj_menu(naglowek, pozycje)
        poprawny = "TEST:\n  1: a\n  2: b"
        assert wynik == poprawny

    def test_dodaj(self):
        obiekt = self.__menu
        element = (3, 'c')
        self.__menu.dodaj(obiekt, element)
        wynik = self.__menu.test_podaj_pozycje()
        poprawny = [(3, 'c'), (8, 'Moduły')]
        assert wynik == poprawny

    def test_usun_pozycje(self):
        obiekt = self.__menu
        element = (3, 'c')
        self.__menu.dodaj(obiekt, element)
        self.__menu.usun_pozycje(3)
        wynik = self.__menu.test_podaj_pozycje()
        poprawny = [(8, 'Moduły')]
        assert wynik == poprawny

    def test_duplikaty_i_sort(self):
        obiekt = self.__menu
        element = (3, 'c')
        self.__menu.dodaj(obiekt, element)
        element = (1, 'a')
        self.__menu.dodaj(obiekt, element)
        element = (3, 'b')
        self.__menu.dodaj(obiekt, element)
        wynik = self.__menu.test_podaj_pozycje()
        poprawny = [(1, 'a'), (2, 'b'), (3, 'c'), (8, 'Moduły')]
        assert wynik == poprawny

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
