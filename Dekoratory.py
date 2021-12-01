# def zwykłaFunkcja():
#     print("To jest zwykła funkcja")
#
# def dekor(funkcja):
#     def wew():
#         print("Dekorujemy funkcję")
#         return funkcja()
#
#     return wew
#
#
# nowaFunkcja = dekor(zwykłaFunkcja)
# nowaFunkcja()


# def dekor(funkcja):
#
#     def wew():
#         print("Dekorujemy funkcję")
#         return funkcja()
#
#     return wew
#
# @dekor
# def zwykłaFunkcja():
#     print("To jest zwykła funkcja")
#
#
# zwykłaFunkcja()

def dekor(funkcja):
    def wew(*args, **kwargs):
        print("Dekorujemy funkcję dodajac kolejny parametr")
        # return funkcja(*args, **kwargs)
        return funkcja(*args, **kwargs)

    return wew


@dekor
def zwyklaFunkcja(*args):
    print("To jest zwykła funkcja, która dodaje liczby:")
    print(sum(args))


zwyklaFunkcja(1, 2, 3, 4, 5, 6, 4, 2, 12, 324, 12)
