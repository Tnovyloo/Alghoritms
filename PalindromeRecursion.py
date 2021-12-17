palindrom =  input('Podaj palindrom').lower()

def sprawdz_palindrom(palindrom):
    print(palindrom)
    if len(palindrom) == 1 or 0:
        return 0
    if palindrom[0] == palindrom[-1]:
        return sprawdz_palindrom(palindrom[1:-1])
    else:
        return f'{palindrom} to nie palindrom'

sprawdz_palindrom(palindrom)