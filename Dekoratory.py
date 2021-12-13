def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcję dodajac kolejny parametr")
        # return funkcja(*args, **kwargs)
        return funkcja(*args, **kwargs) #Funkcja wew zwraca funkcje

    return wew #zwroc wewnetrzna funkcje wew


@dekor #dekor(zwyklafunkcje)
def zwyklaFunkcja(*args):
    print("To jest zwykła funkcja, która dodaje liczby:")
    print(sum(args))


zwyklaFunkcja(1, 2, 3, 4, 5, 6, 4, 2, 12, 324, 12)
