def wypisz(tab):  # tworzymy metode do wypiswania zawartosci naszej tablicy
    for el in tab:
        print(el, end=" | ")


def sortuj_wstaw(tab, n):  # tworzymy metode do sortowania poprzez wstawianie
    for x in range(1, n):
        selected = tab[x]  # aktualnie wybrany element
        y = x - 1  # przygotowujemy iteracje poprzez pozostale elementy
        while y >= 0 and selected < tab[
            y]:  # dopoki nie znajdziemy elementu mniejszego od wybranego i nie natrafimy na poczatek tablicy
            tab[y + 1] = tab[y]  # zamieniamy elementy miejscami
            y -= 1  # modyfikujemy zmienna iteracyjna
        print("\nKrok ", (x - 1), ": przenoszenie elementu  ", selected, " z pozycji ", x, " na pozycje ", (y + 1))
        tab[y + 1] = selected  # po znalezieniu mniejszego elementu, zamieniamy go z wybranym
        wypisz(tab)


print("Podaj ilosc elementow tablicy:")
a = int(input())
tablica = []
for i in range(a):
    print("Podaj element nr. ", (i + 1))
    tablica.append(int(input()))
print("Oto twoja tablica:")
wypisz(tablica)
sortuj_wstaw(tablica, a)
print("Oto twoja tablica po sortowaniu:")
wypisz(tablica)

##ANALIZA KODU
