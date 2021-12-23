from random import randint
#Ta funkcja bieze ostatni element jako pivot,ustawia element pivota
#jako poprawna pozycje w sortowanej liscie, zmienia pozycje elementow
#mniejszych od pivota na lewo, a wiekszych na prawo od pivota
def partition(arr, low, high):
    i = (low - 1) #Najmniejszy indeks
    pivot = arr[high]

    for j in range(low, high):
        #Jesli biezacy element jest mniejszy lub rowny do pivota
        if arr[j] <= pivot:
            #Inkrementuj index mniejszego elementu
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

#Glowna funkcja ktora implementuje QuickSort

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        #pi jest partycja indeksu, arr[p] jest teraz na wlasciwej pozycji
        pi = partition(arr, low, high)

        #Separuj sortowane elementy przed partycją i po partycji
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def generateArray():
    arr = []
    for x in range(100):
        i = randint(0,100)
        arr.append(i)

    return arr

arr = generateArray()
n = len(arr)
quickSort(arr, 0, n-1)
print("Posortowana lista to:")
for i in range(n):
    print(arr[i])