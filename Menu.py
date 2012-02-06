class Menu:

    __pozycje = [(9, 'wyjscie'), (8, 'lista modulow')]
    __zaladowane_obiekty = None

    def pokaz_menu(self):
        print "MENU:"
        for i in self.__pozycje:
            print "%d: %s" % (i[0], i[1])
        print "\n"
        #self.__wybor_elementu()

    def dodaj_do_menu(self, element):
        self.__pozycje.append(element)
        self.__pozycje.sort()

    def __wybor_elementu(self):
        wybor = raw_input('> ')
        if wybor == 1:
            pass

    def przekaz_zaladowane_obiekty(self, zaladowane):
        self.__zaladowane_obiekty = zaladowane
