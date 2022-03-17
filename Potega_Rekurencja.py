def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp-1)

print(power(base=int(input('Podaj liczbe: ')), exp=int(input('Podaj wykładnik: '))))

#same xD
print(pow(10, 10))