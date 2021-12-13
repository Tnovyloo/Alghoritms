def Szukanie_Binarne(target, array):
    min = 0
    max = len(array)
    index = 0
    steps = 0

    while min < max:
        index = (min + max) // 2

        if array[index] == target:
            steps += 1
            return index, steps
        else:
            if array[index] < target:
                steps += 1
                min =  index + 1
            else:
                steps += 1
                max = index

    return - 1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
target = 59

print(Szukanie_Binarne(target, primes))
print(primes[Szukanie_Binarne(target, primes)[0]])

##Ilosc krokow podjetych poprzez szukanie binarne mozna okreslic nastepujacym wzorem, log2(suma dlugosci tablicy) zaokraglajac w górę