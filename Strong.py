
def silnia(n):
    temp = 1 #Domyslnie nasz wynik jest jedynką
    for i in range(2, n + 1): #Dla i w dlugości od dwóch do 'n'
        temp *= i #Wynik * i
    return temp #Zwroć wynik

n = int(input("Podaj liczbe i oblicze z niej silnie: "))
print(silnia(n))

def silnia_rekurencyjna(n):
    if n > 1: #Jezeli n > 1 = Sprawdzamy warunek rekurencji
        return n * silnia_rekurencyjna(n - 1) #Jezli prawda to zwracamy N * funkcja(n - 1)
    return 1 #Zwroc 1

n = int(input("Podaj liczbe i oblicze z niej silnie: "))
print(silnia_rekurencyjna(n))