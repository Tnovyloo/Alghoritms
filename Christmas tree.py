def drukuj_choinki(wysokosc, znak='#'):
    """Drukuj choinke"""
    for i in range(wysokosc):
        print(' ' * (wysokosc - i - 1) + znak * (2 * i + 1))

def choinka(ilosc, wysokosc, znak):
    """Program"""
    for j in range(ilosc):
        drukuj_choinki(wysokosc=wysokosc, znak=znak)

userinput = input("Podaj w nastepujacej kolejnosci"
                  " po spacji ilosc\wielkosc\znak: ")

inputs = [x for x in userinput.split(' ')]
choinka(ilosc=int(inputs[0]), wysokosc=int(inputs[1]), znak=inputs[2])