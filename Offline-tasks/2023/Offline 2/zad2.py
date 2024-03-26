# Jakub Płowiec
# Tak naprawdę w tym zadaniu nie ma znaczenia większosc zasad podanych w zadaniu. Wystarczy posortować i zbierać od najwiekszych kupek te zasoby
# Jest to dosc ciezkie do uzasadnienia natomiast zauwazylem, iz pomimo faktu ze zbieramy od tych najwiekszych kupek to nie wpływa to na zadne straty
# Branie najwiekszych kupek jest najbardziej oplacalne. W teorii możemy przejechac i zniszczyc pola ale to tylko teoria. W kazdym dniu
# Tracimy -1 objętości na każdym polu. W zadaniu rzekomo zaczynamy zbierać od największej kupki ale właściwie to po prostu ułatwia nam obliczenia
# Zlozonosc Czasowa O(n+k), pamieciowa: O(max(n, k))

from zad2testy import runtests


def counting_sort(S, k, B):
    n = len(S)
    C = [0] * k
    for x in S:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[C[S[i]]-1] = S[i]
        C[S[i]] -= 1


def snow( S ):
    n = len(S)
    B = [0] * n

    k = 0
    for i in range(n):
        if k < S[i]:
            k = S[i]

    counting_sort(S, k+1, B)

    result = 0
    i = n-1
    k = 0
    while True:
        if i < 0 or B[i] - k <= 0:
            break
        result += B[i] - k
        i -= 1
        k += 1
    return result


runtests( snow, all_tests = False )
