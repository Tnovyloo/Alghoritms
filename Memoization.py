factorial_dict = {}

def factorial_memo(input_value):
    #Pierwszy warunek
    if input_value < 2:
        return 1
    #Jesli wartosci nie ma w dict to kontynuuj
    if input_value not in factorial_dict:
        factorial_dict[input_value] = input_value * factorial_memo(input_value - 1)
        return factorial_dict[input_value]

print(factorial_memo(5))

##Drugi sposób
from functools import lru_cache

@lru_cache(maxsize=1000)
def factorial(input_value):
    if input_value < 2:
        return 1
    elif input_value >= 2:
        return input_value * factorial(input_value - 1)

for i in range(1, 100):
    print(f"{i}! = ", factorial(i))


#https://towardsdatascience.com/mastering-memoization-in-python-dcdd8b435189