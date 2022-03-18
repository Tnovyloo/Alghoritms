import random

def mergesort(array):
    if len(array) > 1:
        #Szukamy środka listy
        mid = len(array) // 2
        #Dzielimy liste
        L = array[:mid]
        #Na dwie części
        R = array[mid:]
        #Sortujemy pierwszą część
        mergesort(L)
        #Sortujemy drugą część
        mergesort(R)
        i = j = k = 0
        #Kopiuj wartości do temp. list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        #Sprawdź jeśli jakis element został wyrzucony
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

def random_list(list_len):
    func_list = [random.randint(0,1000) for i in range(list_len)]
    return func_list

# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergesort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    # print(lambda x: random.randint(0,1000) for x in range(100))
