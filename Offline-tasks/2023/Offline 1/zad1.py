# Jakub Płowiec
# Prosty i raczej oczywisty algorytm. Skoro długość musi być nieparzysta w takim razie wystarczy przelecieć stringa po każdej literce jako środek
# i sprawdzać czy lewa strona == prawa strona. Jezeli tak to badamy nastepne cyfry czy są takie same. Jezeli nie, mamy obliczona dlugosc stringa
# i potem uzywamy maxa.
# Zlozonosc czasowa: O(n^2), pamieciowa: O(1)
from zad1testy import runtests
def ceasar( s ):
    n = len(s)

    if n < 2:
        return n

    result = 1

    for k in range(n):
        i = k - 1
        j = k + 1
        while i >= 0 and j < n and s[i] == s[j]:
            i = i - 1
            j = j + 1
        length = j - i - 1
        if result < length:
            result = length

    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
