class Wezel():
    def __init__(self, dane=None):
        self.dane = dane
        self.lewe_dziecko = None
        self.prawe_dziecko = None

class BST():
    def __init__(self):
        self.korzen = Wezel()

    def Dodaj(self, dane):
        if self.korzen.dane is None:
            self.korzen.dane = dane
        else:
            def Dodaj_Do_Wierzcholka(dane, wierzcholek):
                if dane < wierzcholek.dane:
                    if wierzcholek.lewe_dziecko is None:
                        wierzcholek.lewe_dziecko = Wezel(dane)
                    else:
                        Dodaj_Do_Wierzcholka(dane, wierzcholek.lewe_dziecko)

                if dane > wierzcholek.dane:
                    if wierzcholek.prawe_dziecko is None:
                        wierzcholek.prawe_dziecko = Wezel(dane)
                    else:
                        Dodaj_Do_Wierzcholka(dane, wierzcholek.prawe_dziecko)

            Dodaj_Do_Wierzcholka(dane, self.korzen)

    def Wyswietl(self):
        wynik = ''
        def Przechodzenie_Wzdluzne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik += (str(wierzcholek.dane) + "-")
                    wynik = Przechodzenie_Wzdluzne(wynik, wierzcholek.lewe_dziecko)
                    wynik = Przechodzenie_Wzdluzne(wynik, wierzcholek.prawe_dziecko)
            return wynik

        def Przechodzenie_Poprzeczne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = Przechodzenie_Poprzeczne(wynik, wierzcholek.lewe_dziecko)
                    wynik += (str(wierzcholek.dane) + "-")
                    wynik = Przechodzenie_Poprzeczne(wynik, wierzcholek.prawe_dziecko)
            return wynik

        def Przechodzenie_Wsteczne(wynik, wierzcholek):
            if wierzcholek:
                if wierzcholek.dane:
                    wynik = Przechodzenie_Wsteczne(wynik, wierzcholek.lewe_dziecko)
                    wynik = Przechodzenie_Wsteczne(wynik, wierzcholek.prawe_dziecko)
                    wynik += (str(wierzcholek.dane) + "-")
            return wynik

        print(Przechodzenie_Wzdluzne(wynik, self.korzen))
        print(Przechodzenie_Poprzeczne(wynik, self.korzen))
        print(Przechodzenie_Wzdluzne(wynik, self.korzen))

drzewo = BST()
drzewo.Dodaj(3)
drzewo.Dodaj(2)
drzewo.Dodaj(1)
drzewo.Dodaj(8)
drzewo.Dodaj(7)
drzewo.Dodaj(99)

drzewo.Wyswietl()