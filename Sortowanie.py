def wypisz(tab):  # tworzymy metode do wypiswania zawartosci naszej tablicy
    for el in tab:
        print(el, end=" | ")

def sortowanie(tab, n):
    for x in range(1, n):
        selected = tab[n]
        y = x - 1
        while y >= 0 and selected < tab[y]:
            tab[y + 1] = tab[y]
            y -= 1
        print("\nKrok ", (x - 1), ": przenoszenie elementu  ", selected, " z pozycji ", x, " na pozycje ", (y + 1))
        tab[y + 1] = selected

print("Podaj ilosc elementow tablicy:")
a = int(input())
tablica = []
for i in range(a):
    print("Podaj element nr. ", (i + 1))
    tablica.append(int(input()))
print("Oto twoja tablica:")
wypisz(tablica)
sortowanie(tablica, a)
print("Oto twoja tablica po sortowaniu:")
wypisz(tablica)
