from functools import lru_cache

@lru_cache(maxsize=1000)
def TowerOfHanoi(n, source, destination, auxiliary):
    #Warunek rekurencji
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    TowerOfHanoi(n - 1, auxiliary, destination, source)

n = 64
TowerOfHanoi(n=n, source='A', destination='B', auxiliary='C')