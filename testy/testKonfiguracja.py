'''
Created on 18-02-2012

@author: loper
'''
import unittest
from Konfiguracja import Konfiguracja


class Test(unittest.TestCase):

    def test_podaj_wartosc(self):
        konf = Konfiguracja('test_ustawienia.cfg')
        uzyt = konf.podaj_wartosc('uzytkownik')
        nagl = konf.podaj_wartosc('naglowek')
        wers = konf.podaj_wartosc('wersja')

        del konf

        self.assertEqual(uzyt, "tester")
        self.assertEqual(nagl, "UnitTest")
        self.assertEqual(wers, '9.4')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_podaj_wartosc']
    unittest.main()
