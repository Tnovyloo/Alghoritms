from random import randint
from functools import reduce

#using lambda
square = lambda x: x ** 2
print(square(10))

points2d = [(1, 2), (15, 1), (5, 1), (10, 4)]
points2d_sorted = sorted(points2d, key=lambda x: x[1])

print(points2d_sorted)

#creating random numbers list
random_numbers = sorted([randint(1,100) for x in range(51)]) # creating random numbers list
print(random_numbers)

#map function
testing_map = map(lambda x: x**2, random_numbers)
print(list(testing_map))

#other way with no map
testing_map_2 = [x**2 for x in random_numbers]
print(testing_map_2)

#filter function
testing_filter = filter(lambda x: x%2==0, random_numbers)
print(list(testing_filter))

#other way to not use filter function
testing_filter_2 = [x for x in random_numbers if x%2==0]
print(testing_filter_2)

#reduce func
testing_reduce = reduce(lambda x, y: x*y, random_numbers)
print(testing_reduce)