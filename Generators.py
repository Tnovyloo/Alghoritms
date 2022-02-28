# def generator():
#     yield 1
#     yield 2
#     yield 3
#
# g = generator()
# value = print(next(g))
# value = print(next(g))
# value = print(next(g))
#
# print(sum(g))
#
# c = generator()
# print(sum(c))
#
# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1
#
# cd = countdown(100)

def numbers(num):
    numbers_list = []
    n = 0
    while n < num:
        numbers_list.append(num)
        n += 1
    return numbers_list

print(sum(numbers(971)))

def numbers_generator(num):
    n = 0
    while n < num:
        yield n
        n += 1

print(sum(numbers_generator(971)))

def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = [print(a) for a in fibonacci(30)]

g = (i for i in range(1000) if i % 2 == 0)

for i in g:
    print(i)